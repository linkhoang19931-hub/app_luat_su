# App Ôn Thi Luật Sư (SwiftUI)

Dự án dành riêng cho vợ yêu ôn thi chứng chỉ hành nghề Luật sư.

## 🚀 Hướng dẫn thiết lập (Dành cho máy Mac)

1. **Khởi tạo Project:**
   - Mở Xcode -> File -> New -> Project -> iOS App.
   - Name: `AppLuatSu`.
   - Interface: `SwiftUI`.
   - Language: `Swift`.

2. **Thêm mã nguồn:**
   - Copy các thư mục `Models`, `Views`, `ViewModels` từ repository này vào project Xcode của bạn.
   - Lưu ý chọn **"Create groups"** khi kéo vào Xcode.

3. **Thêm dữ liệu câu hỏi:**
   - Kéo file `questions.json` vào thư mục `Resources` trong Xcode.
   - **QUAN TRỌNG:** Phải tích vào ô **"Add to targets: AppLuatSu"** để ứng dụng có thể đọc được file.

4. **Chạy ứng dụng:**
   - Chọn Simulator (ví dụ iPhone 15) và nhấn `Cmd + R` để chạy.

## 📂 Cấu trúc dự án (MVVM)
- `Models/`: Định nghĩa cấu trúc dữ liệu `Question`.
- `ViewModels/`: Logic xử lý load câu hỏi, tính điểm, chuyển câu.
- `Views/`: Giao diện người dùng (Main View, Question View, Result View).
- `Resources/`: Chứa file `questions.json`.

## 🛠 Công cụ hỗ trợ dữ liệu (Dành cho máy Windows)
- `extract_pdf.py`: Script Python dùng để trích xuất nội dung từ file PDF tài liệu ôn thi FDVN (602 trang).
- `extracted_text.txt`: File văn bản sau khi trích xuất để AI phân tích và chuyển đổi thành JSON.

---
*Chúc vợ thi tốt và sớm trở thành Luật sư thực thụ! ⚖️*
