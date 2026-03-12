import json
import os
import re

input_dir = "data/documents"
output_file = "AppLuatSu/Resources/questions_data.json"

def extract_md_from_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            pdf_base = os.path.basename(file_path).replace(".md", "")
            return data.get("formats", {}).get("markdown", {}).get("content", ""), pdf_base
    except: return "", ""

def parse_all_content():
    exams = []
    
    for filename in sorted(os.listdir(input_dir)):
        if filename.endswith(".md"):
            md_content, pdf_base = extract_md_from_json(os.path.join(input_dir, filename))
            if not md_content: continue
            
            # 1. Tìm tất cả Page Markers
            page_markers = list(re.finditer(r'## Page (\d+)', md_content))
            
            # 2. Tìm tất cả Exam Titles
            exam_markers = list(re.finditer(r'\*\*(Đề\s+(?:Kiểm tra|thi)\s+.*?)\*\*', md_content, flags=re.IGNORECASE))
            
            # 3. Tìm tất cả Question Titles
            q_markers = list(re.finditer(r'\*\*(Câu\s+\d+.*?)\*\*', md_content))
            
            # Helper function để lấy danh sách trang giữa 2 vị trí
            def get_pages_in_range(start, end):
                pages = []
                # Lấy trang bắt đầu (trang chứa vị trí start)
                start_page = 1
                for p in reversed(page_markers):
                    if p.start() <= start:
                        start_page = int(p.group(1))
                        break
                pages.append(f"{pdf_base}_page_{start_page}.pdf")
                
                # Lấy các trang trung gian và trang cuối
                for p in page_markers:
                    if start < p.start() < end:
                        p_num = int(p.group(1))
                        p_file = f"{pdf_base}_page_{p_num}.pdf"
                        if p_file not in pages:
                            pages.append(p_file)
                return pages

            # Xử lý Exams
            for i, ex in enumerate(exam_markers):
                start = ex.start()
                end = exam_markers[i+1].start() if i+1 < len(exam_markers) else len(md_content)
                
                # Tìm trang của Exam
                pdf_pages = get_pages_in_range(start, end)
                
                exam_obj = {
                    "title": ex.group(1),
                    "pdf_pages": pdf_pages,
                    "questions": []
                }
                
                # Tìm các câu hỏi thuộc Exam này
                current_q_markers = [q for q in q_markers if start <= q.start() < end]
                
                for j, q in enumerate(current_q_markers):
                    q_start = q.start()
                    q_end = current_q_markers[j+1].start() if j+1 < len(current_q_markers) else end
                    
                    q_pdf_pages = get_pages_in_range(q_start, q_end)
                    q_content = md_content[q_start:q_end].replace(q.group(0), "").strip()
                    
                    # Clean up: loại bỏ các "## Page X" markers khỏi nội dung text
                    q_content = re.sub(r'## Page \d+', '', q_content).strip()

                    exam_obj["questions"].append({
                        "id": j + 1,
                        "title": q.group(1),
                        "content": q_content,
                        "pdf_pages": q_pdf_pages,
                        "answer_guideline": "Bấm '💡 Xem đáp án' để xem chi tiết hoặc đối chiếu trực tiếp với PDF bên cạnh."
                    })
                
                if exam_obj["questions"]: # Chỉ add nếu có câu hỏi
                    exams.append(exam_obj)
                    
    return exams

if __name__ == "__main__":
    print("Bắt đầu cập nhật dữ liệu hỗ trợ nhiều trang PDF...")
    exams = parse_all_content()
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(exams, f, ensure_ascii=False, indent=2)
    print(f"Xong! Đã xử lý {len(exams)} bộ đề.")
