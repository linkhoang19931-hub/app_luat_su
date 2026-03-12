import json
import os
import re

input_dir = "data/documents"
output_file = "AppLuatSu/Resources/questions_data.json"

def extract_md_from_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Lưu tên file gốc để biết thuộc part nào (p1_1, p2, p3...)
            pdf_base = os.path.basename(file_path).replace(".md", "")
            return data.get("formats", {}).get("markdown", {}).get("content", ""), pdf_base
    except: return "", ""

def parse_all_content():
    exams = []
    
    for filename in sorted(os.listdir(input_dir)):
        if filename.endswith(".md"):
            md_content, pdf_base = extract_md_from_json(os.path.join(input_dir, filename))
            if not md_content: continue
            
            # Tách nội dung theo trang: ## Page X
            pages = re.split(r'## Page (\d+)', md_content)
            
            for i in range(1, len(pages), 2):
                page_num = int(pages[i])
                page_text = pages[i+1]
                
                # Tìm Đề thi trong trang này
                exam_titles = re.findall(r'\*\*(Đề\s+(?:Kiểm tra|thi)\s+.*?)\*\*', page_text, flags=re.IGNORECASE)
                for title in exam_titles:
                    exams.append({
                        "title": title,
                        "pdf_page_file": f"{pdf_base}_page_{page_num}.pdf", # Trỏ thẳng trang lẻ
                        "questions": []
                    })
                
                # Nếu có câu hỏi trong trang này, gán vào đề thi gần nhất
                q_titles = re.findall(r'\*\*(Câu\s+\d+.*?)\*\*', page_text)
                if exams and q_titles:
                    for q_title in q_titles:
                        q_content_match = re.search(f'\\*\\*{re.escape(q_title)}\\*\\*(.*?)(?=\\*\\*Câu|$)', page_text, re.DOTALL)
                        q_content = q_content_match.group(1) if q_content_match else ""
                        
                        exams[-1]["questions"].append({
                            "id": len(exams[-1]["questions"]) + 1,
                            "title": q_title,
                            "content": q_content.strip(),
                            "pdf_page_file": f"{pdf_base}_page_{page_num}.pdf", # Trỏ thẳng trang lẻ
                            "answer_guideline": "Bấm '💡 Xem đáp án' để xem chi tiết hoặc đối chiếu trực tiếp với PDF bên cạnh."
                        })
    return exams

if __name__ == "__main__":
    print("Bắt đầu cập nhật dữ liệu để dùng trang PDF lẻ...")
    exams = parse_all_content()
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(exams, f, ensure_ascii=False, indent=2)
    print("Xong!")
