# Nhật ký Tiến độ Dự án - App Ôn Thi Luật Sư

## 🚀 Trạng thái Hiện tại: Web MVP (Pro Dual View)
Dự án đã chuyển trọng tâm sang hoàn thiện bản Web để phục vụ việc ôn tập tức thì, với tính năng xem câu hỏi song hành cùng tài liệu PDF gốc.

---

## ✅ Các công việc đã hoàn thành & Commit

### 1. Xử lý Dữ liệu & PDF (Data Engineering)
- [x] **Tách PDF lẻ:** Đã tách toàn bộ các file PDF tài liệu (hơn 1000 trang) thành từng trang riêng biệt trong thư mục `data/pages/`. Việc này giúp bản Web load tài liệu siêu tốc và chính xác.
- [x] **Script Tự động hóa:** 
    - `split_to_pages.py`: Tự động quét và tách mọi file PDF trong `data/`.
    - `super_convert.py`: Quét các file Markdown (từ `data/documents/`), trích xuất câu hỏi và tự động ánh xạ (mapping) chúng với đúng file PDF trang lẻ tương ứng.
- [x] **Cập nhật JSON:** File `AppLuatSu/Resources/questions_data.json` đã được cập nhật cấu trúc mới, chứa đầy đủ thông tin: Tiêu đề đề thi, nội dung câu hỏi, gợi ý giải và link file PDF trang lẻ.

### 2. Phát triển Web (Frontend)
- [x] **Giao diện Dual View:** Thiết kế 3 cột: 
    - Cột 1: Danh sách bộ đề.
    - Cột 2: Nội dung câu hỏi & Gợi ý giải (Markdown support).
    - Cột 3: Trình xem PDF trang lẻ (Tự động fit-to-width).
- [x] **Dark Mode:** Hỗ trợ giao diện tối để ôn thi ban đêm không mỏi mắt.
- [x] **Tính năng Xem đáp án:** Ẩn/hiện gợi ý giải bài ngay tại giao diện câu hỏi.

### 3. Cấu trúc iOS (SwiftUI)
- [x] **Model Update:** Đã cập nhật `Question.swift` và `QuizViewModel.swift` để tương thích với cấu trúc JSON mới (hiện đang tạm dừng để ưu tiên Web).

---

## 📌 Các Commit Quan trọng
- `def6957`: Cập nhật `GEMINI.md` ưu tiên Web, đồng bộ mapping PDF trang lẻ vào JSON.
- `7d7a1dd`: Hoàn tất tách PDF, thêm các script xử lý dữ liệu tự động.
- `d9a7c01`: Major Update - Thêm Dark Mode, tối ưu layout Dual View và PDF fitting.
- `6da5441`: Fix lỗi cuộn (scrolling) và tối ưu giao diện cột.

---

## 🛠 Hướng dẫn Chạy local (Web)
1. Mở file `index.html` bằng trình duyệt (Nên dùng Live Server trong VS Code để tránh lỗi CORS khi load JSON).
2. Chọn bộ đề bên tay trái.
3. Câu hỏi sẽ hiện ở giữa và trang PDF tài liệu gốc sẽ hiện ngay bên phải.

---
*Cập nhật lần cuối: 12/03/2026 - Gemini CLI*
