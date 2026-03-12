import re

file_path = "full_exam_text.txt"
mcq_count = 0

try:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        # Tìm mẫu A. B. C. D.
        # Một câu trắc nghiệm điển hình thường có ít nhất 3 lựa chọn
        patterns = re.findall(r"(?:[A-D]\.\s+.*\n?){3,}", content)
        mcq_count = len(patterns)
        print(f"Số lượng khối trắc nghiệm tìm thấy: {mcq_count}")
        if mcq_count > 0:
            print("Ví dụ 3 khối đầu tiên:")
            for p in patterns[:3]:
                print("-" * 20)
                print(p)
except Exception as e:
    print(f"Lỗi: {e}")
