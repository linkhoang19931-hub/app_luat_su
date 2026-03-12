import json
import os
import re

input_dir = "data/documents"
output_file = "AppLuatSu/Resources/questions_data.json"

def extract_md_from_json(file_path):
    """Nanonets trả về JSON, cần lấy trường content của markdown."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("formats", {}).get("markdown", {}).get("content", "")
    except Exception as e:
        print(f"Lỗi khi đọc {file_path}: {e}")
        return ""

def parse_markdown(content):
    """
    Phân tích nội dung Markdown để bóc tách Đề thi, Câu hỏi và Đáp án.
    Đây là một logic heuristic (phỏng đoán) dựa trên cấu trúc tài liệu FDVN.
    """
    exams = []
    # Tìm các mốc "Đề Kiểm tra" hoặc "Đề thi"
    # Ví dụ: **Đề Kiểm tra Viết**
    exam_sections = re.split(r'\*\*Đề\s+(?:Kiểm tra|thi)\s+.*?\*\*', content, flags=re.IGNORECASE)
    exam_titles = re.findall(r'\*\*(Đề\s+(?:Kiểm tra|thi)\s+.*?)\*\*', content, flags=re.IGNORECASE)
    
    for i, title in enumerate(exam_titles):
        if i + 1 < len(exam_sections):
            exam_body = exam_sections[i+1]
            
            # Trích xuất ngày tháng
            date_match = re.search(r'ngày\s+\d+\s+tháng\s+\d+\s+năm\s+\d+', exam_body)
            date = date_match.group(0) if date_match else "Không rõ ngày"
            
            # Tách các câu hỏi: Tìm "Câu 1", "Câu 2"...
            question_sections = re.split(r'\*\*Câu\s+\d+.*?\*\*', exam_body)
            question_titles = re.findall(r'\*\*(Câu\s+\d+.*?)\*\*', exam_body)
            
            questions = []
            for j, q_title in enumerate(question_titles):
                if j + 1 < len(question_sections):
                    q_content = question_sections[j+1].strip()
                    # Tách phần Đáp án nếu có (FDVN thường ghi "Gợi ý đáp án" hoặc tương tự)
                    parts = re.split(r'Gợi ý đáp án|Đáp án mẫu|Hướng dẫn giải', q_content, flags=re.IGNORECASE)
                    
                    questions.append({
                        "id": j + 1,
                        "title": q_title,
                        "content": parts[0].strip(),
                        "answer_guideline": parts[1].strip() if len(parts) > 1 else "Xem tài liệu FDVN để biết chi tiết."
                    })
            
            exams.append({
                "id": i + 1,
                "title": title,
                "date": date,
                "questions": questions
            })
            
    return exams

def main():
    all_exams = []
    if not os.path.exists("AppLuatSu/Resources"):
        os.makedirs("AppLuatSu/Resources")

    for filename in sorted(os.listdir(input_dir)):
        if filename.endswith(".md"):
            print(f"Đang xử lý {filename}...")
            file_path = os.path.join(input_dir, filename)
            md_content = extract_md_from_json(file_path)
            if md_content:
                exams = parse_markdown(md_content)
                all_exams.extend(exams)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_exams, f, ensure_ascii=False, indent=2)
    
    print(f"Hoàn thành! Đã tạo file dữ liệu: {output_file}")
    print(f"Tổng cộng tìm thấy: {len(all_exams)} đề thi.")

if __name__ == "__main__":
    main()
