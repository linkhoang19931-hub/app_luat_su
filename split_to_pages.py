import pypdf
import os

data_dir = "data"
output_dir = "data/pages"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def split_all_to_pages():
    for filename in os.listdir(data_dir):
        if filename.endswith(".pdf") and not filename.startswith("p1_1_page"):
            print(f"Đang tách file: {filename}...")
            file_path = os.path.join(data_dir, filename)
            try:
                reader = pypdf.PdfReader(file_path)
                for i in range(len(reader.pages)):
                    writer = pypdf.PdfWriter()
                    writer.add_page(reader.pages[i])
                    
                    page_filename = f"{filename.replace('.pdf', '')}_page_{i+1}.pdf"
                    with open(os.path.join(output_dir, page_filename), "wb") as f:
                        writer.write(f)
                print(f"Xong {filename}: {len(reader.pages)} trang.")
            except Exception as e:
                print(f"Lỗi {filename}: {e}")

if __name__ == "__main__":
    split_all_to_pages()
