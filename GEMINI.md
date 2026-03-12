# App Ôn Thi Luật Sư - Project Documentation

## 1. Vai trò của Gemini CLI
Tôi là **Senior Full-stack Developer** (Chuyên gia iOS/SwiftUI & Kiến trúc sư Backend) chịu trách nhiệm toàn diện trong việc thiết kế, xây dựng và tối ưu hóa ứng dụng này. Tôi sẽ hỗ trợ bạn từ khâu lên ý tưởng, code giao diện, xử lý dữ liệu đến khi sẵn sàng publish lên App Store.

## 2. Mục tiêu dự án
Xây dựng một ứng dụng iOS bản địa (Native) chuyên nghiệp, tập trung vào trải nghiệm người dùng (UX) mượt mà để giúp vợ của bạn ôn thi chứng chỉ hành nghề Luật sư hiệu quả nhất.

## 3. Kiến trúc kỹ thuật (Đề xuất)
- **Frontend (iOS):** SwiftUI (Hiện đại, tối ưu cho iOS 15+).
- **Backend:** 
  - Giai đoạn 1 (MVP): Sử dụng file local JSON hoặc SQLite để chạy Offline (vợ bạn có thể học mọi lúc mọi nơi).
  - Giai đoạn 2 (Scale): Cloud database (Firebase hoặc Supabase) để đồng bộ kết quả, thống kê điểm số giữa các thiết bị.
- **Dữ liệu:** Dựa trên file `questions.json` đã có sẵn.

## 4. Các tính năng chính (Core Features)

### A. Chế độ học tập (Learning Mode)
- **Ôn tập theo chủ đề:** (Hình sự, Dân sự, Đạo đức nghề nghiệp, Hành chính...).
- **Giải thích chi tiết:** Hiển thị `explanation` ngay sau khi chọn đáp án để ghi nhớ kiến thức.

### B. Chế độ thi thử (Mock Exam)
- **Thi theo thời gian:** Tạo đề thi ngẫu nhiên với số lượng câu hỏi và thời gian như thi thật.
- **Chấm điểm & Đánh giá:** Phân tích những mảng kiến thức còn yếu để tập trung ôn luyện.

### C. Theo dõi tiến độ (Progress Tracking)
- Lưu lịch sử thi, số câu đúng/sai.
- Biểu đồ tiến độ học tập hàng tuần.

### D. Flashcards & Ghi chú
- Đánh dấu các câu hỏi khó để ôn lại riêng.

## 5. Lộ trình triển khai (Roadmap)
1. **Research & UI Design:** Thiết kế giao diện (Mockup) trong SwiftUI.
2. **Data Layer:** Xây dựng logic đọc dữ liệu từ `questions.json`.
3. **Core Engine:** Logic làm bài trắc nghiệm, tính điểm.
4. **Analysis:** Tính năng thống kê và lịch sử.
5. **Publishing:** Tối ưu hóa hiệu năng, chuẩn bị metadata cho App Store.

---
*Ghi chú: Mọi quyết định về kiến trúc sẽ ưu tiên sự đơn giản, tin cậy và thẩm mỹ đúng chuẩn ứng dụng iOS.*
