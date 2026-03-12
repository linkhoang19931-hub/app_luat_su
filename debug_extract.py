import json

file_path = "data/documents/p1_1.md"
output_path = "p1_1_full.md"

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        content = data.get("formats", {}).get("markdown", {}).get("content", "")
        with open(output_path, 'w', encoding='utf-8') as out:
            out.write(content)
    print(f"Đã trích xuất xong Markdown vào {output_path}")
except Exception as e:
    print(f"Lỗi: {e}")
