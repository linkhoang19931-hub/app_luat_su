# App Ôn Thi Luật Sư - Project Documentation

## 1. Vai trò của Gemini CLI
Tôi là **Senior Full-stack Developer** (Chuyên gia iOS/SwiftUI & Kiến trúc sư Backend) chịu trách nhiệm toàn diện trong việc thiết kế, xây dựng và tối ưu hóa ứng dụng này. Tôi sẽ hỗ trợ bạn từ khâu lên ý tưởng, code giao diện, xử lý dữ liệu đến khi sẵn sàng publish.

## 2. Mục tiêu dự án
Xây dựng một ứng dụng ôn thi chứng chỉ hành nghề Luật sư hiệu quả, tập trung vào trải nghiệm người dùng (UX) mượt mà với tính năng xem tài liệu PDF song hành cùng câu hỏi.

## 3. Kiến trúc kỹ thuật
### A. Web (Ưu tiên hiện tại)
- **Frontend:** HTML5, CSS3 (Vanilla CSS), JavaScript (Vanilla JS).
- **Tính năng đặc biệt:** Pro Dual View - Hiển thị câu hỏi bên trái và trang PDF tương ứng bên phải.
- **Dữ liệu:** File local JSON (`questions_data.json`) được tạo từ việc xử lý các file Markdown/PDF.
- **Tối ưu hóa:** Tách PDF thành từng trang lẻ để tăng tốc độ load và chính xác vị trí tài liệu.

### B. iOS (Giai đoạn sau)
- **Frontend:** SwiftUI (Đang tạm dừng để tập trung hoàn thiện bản Web).
- **Backend:** Local JSON/SQLite (MVP) hoặc Firebase/Supabase (Scale).

## 4. Các tính năng chính (Core Features)
- **Dual View Mode:** Xem câu hỏi và tài liệu gốc (PDF) cùng lúc.
- **Dark Mode:** Hỗ trợ học tập ban đêm, giảm mỏi mắt.
- **Tự động Fit PDF:** PDF tự động hiển thị đúng trang và căn chỉnh vừa vặn màn hình.
- **Tiến độ học tập:** Theo dõi số câu đã làm trong bộ đề.

## 5. Lộ trình triển khai (Roadmap)
1. **[Hoàn thành] PDF Processing:** Tách toàn bộ PDF (hơn 1000 trang) thành các file đơn lẻ.
2. **[Hoàn thành] Data Mapping:** Xây dựng script `super_convert.py` để ánh xạ câu hỏi từ Markdown sang đúng file PDF trang lẻ.
3. **[Đang thực hiện] Web MVP:** Hoàn thiện giao diện Web với tính năng Dual View và Dark Mode.
4. **Data Refinement:** Tiếp tục chuẩn hóa dữ liệu từ các file Markdown còn lại.
5. **iOS Implementation:** Chuyển đổi logic từ Web sang SwiftUI.

---
*Ghi chú: Ưu tiên sự đơn giản, tốc độ và trải nghiệm xem tài liệu song hành là chìa khóa của ứng dụng này.*
