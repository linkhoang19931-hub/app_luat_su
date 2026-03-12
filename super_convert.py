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

def clean_question_content(text):
    text = re.sub(r'<(?:img|page_number|watermark|footer)>.*?</(?:img|page_number|watermark|footer)>', '', text, flags=re.DOTALL)
    text = re.sub(r'## Page \d+', '', text)
    junk_patterns = [
        r'web:\s+fdvn\.vn.*?\n', r'fdvn\.vn\s+---\s+.*?\.vn', r'Tài liệu nghiệp vụ',
        r'LUẬT SƯ FDVN', r'FDVN LAW FIRM', r'Feel free to go with the truth',
        r'BỘ TƯ PHÁP', r'HỘI ĐỒNG KIỂM TRA.*?\n', r'Khu vực Thành Phố.*?\n',
        r'ĐỀ KIỂM TRA VIẾT', r'Kiểm tra:\s+ngày\s+.*?năm\s+\d{4}', r'Thời gian làm bài.*?phút',
    ]
    for p in junk_patterns:
        text = re.sub(p, '', text, flags=re.IGNORECASE)
    return text.strip()

def parse_all_content():
    exams = []
    for filename in sorted(os.listdir(input_dir)):
        if filename.endswith(".md"):
            md_content, pdf_base = extract_md_from_json(os.path.join(input_dir, filename))
            if not md_content: continue
            
            page_markers = list(re.finditer(r'## Page (\d+)', md_content))
            
            exam_markers = list(re.finditer(r'\*\*(Đề\s+(?:Kiểm tra|thi|BÀI KIỂM TRA|BẾ THI)\s+.*?)\*\*', md_content, flags=re.IGNORECASE))
            exam_markers += list(re.finditer(r'# (ĐỀ\s+.*?)\n', md_content, flags=re.IGNORECASE))
            header_markers = list(re.finditer(r'^BỘ TƯ PHÁP', md_content, flags=re.MULTILINE))
            
            q_markers = list(re.finditer(r'\*\*(Câu\s+\d+.*?)\*\*', md_content))
            ans_markers = list(re.finditer(r'# (?:ĐÁP ÁN|BÀI GIẢI|GIẢI ĐỀ).*?\n', md_content, flags=re.IGNORECASE))
            ans_markers += list(re.finditer(r'\*\*(?:ĐÁP ÁN|BÀI GIẢI|GIẢI ĐỀ).*?\*\*', md_content, flags=re.IGNORECASE))

            boundaries = sorted(exam_markers + ans_markers + header_markers, key=lambda x: x.start())

            def get_pages_in_range(start, end):
                pages = []
                start_p = 1
                for p in reversed(page_markers):
                    if p.start() <= start:
                        start_p = int(p.group(1))
                        break
                pages.append(f"{pdf_base}_page_{start_p}.pdf")
                for p in page_markers:
                    if start < p.start() < end:
                        p_num = int(p.group(1))
                        p_file = f"{pdf_base}_page_{p_num}.pdf"
                        if p_file not in pages: pages.append(p_file)
                return pages

            for i, marker in enumerate(boundaries):
                is_exam_start = any(marker.start() == ex.start() for ex in exam_markers) or \
                                any(marker.start() == h.start() for h in header_markers)
                if not is_exam_start: continue
                
                start = marker.start()
                end = boundaries[i+1].start() if i+1 < len(boundaries) else len(md_content)
                
                exam_title = "Đề thi"
                for ex in exam_markers:
                    if ex.start() == marker.start():
                        exam_title = ex.group(1) if hasattr(ex, 'group') else ex.group(0)
                        break

                ans_content_block = ""
                ans_block_start = 0
                ans_block_end = 0
                for j in range(i+1, len(boundaries)):
                    m = boundaries[j]
                    if any(m.start() == ans.start() for ans in ans_markers):
                        ans_block_start = m.start()
                        ans_block_end = boundaries[j+1].start() if j+1 < len(boundaries) else len(md_content)
                        ans_content_block = md_content[ans_block_start:ans_block_end]
                        break
                
                exam_obj = {
                    "title": exam_title.strip().replace("**", ""),
                    "pdf_pages": get_pages_in_range(start, end),
                    "questions": []
                }
                
                current_q_markers = [q for q in q_markers if start <= q.start() < end]
                for j, q in enumerate(current_q_markers):
                    q_start = q.start()
                    q_end = current_q_markers[j+1].start() if j+1 < len(current_q_markers) else end
                    
                    q_title = q.group(0).replace("**", "").strip()
                    q_text = clean_question_content(md_content[q_start:q_end].replace(q.group(0), ""))
                    
                    specific_ans = ""
                    ans_pdf_pages = []
                    if ans_content_block:
                        q_num_match = re.search(r'Câu\s+(\d+)', q_title)
                        if q_num_match:
                            q_num = q_num_match.group(1)
                            # Tìm vị trí của "Câu X" trong khối đáp án để lấy trang PDF
                            ans_q_pattern = rf'(?:Câu|Câu hỏi)\s+{q_num}'
                            ans_q_matches = list(re.finditer(ans_q_pattern, ans_content_block, re.IGNORECASE))
                            if ans_q_matches:
                                a_start = ans_block_start + ans_q_matches[0].start()
                                # Tìm điểm kết thúc là câu đáp án tiếp theo
                                next_ans_q = re.search(rf'(?:Câu|Câu hỏi)\s+\d+', ans_content_block[ans_q_matches[0].end():], re.IGNORECASE)
                                if next_ans_q:
                                    a_end = a_start + next_ans_q.start() + len(ans_q_matches[0].group(0))
                                else:
                                    a_end = ans_block_end
                                
                                ans_pdf_pages = get_pages_in_range(a_start, a_end)
                                specific_ans = clean_question_content(md_content[a_start:a_end].replace(ans_q_matches[0].group(0), ""))

                    exam_obj["questions"].append({
                        "id": j + 1, "title": q_title, "content": q_text,
                        "pdf_pages": get_pages_in_range(q_start, q_end),
                        "answer_guideline": specific_ans or "Xem chi tiết đáp án trong file PDF.",
                        "ans_pdf_pages": ans_pdf_pages or exam_obj["pdf_pages"] # Fallback về trang đề nếu không tìm thấy
                    })
                if exam_obj["questions"]: exams.append(exam_obj)
    return exams

if __name__ == "__main__":
    exams = parse_all_content()
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(exams, f, ensure_ascii=False, indent=2)
    print(f"Xong! Đã cập nhật {len(exams)} bộ đề với mapping PDF đáp án.")
