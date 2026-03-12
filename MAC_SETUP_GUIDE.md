# Hướng dẫn Setup Gemini (User Login) trên macOS

Tài liệu này hướng dẫn cách mang Session đăng nhập (User/Pass) từ máy này sang máy Mac.

## 1. Cài đặt Gemini CLI
Mở Terminal và cài bản CLI bạn đang dùng (giả định là bản hỗ trợ browser login):
```bash
npm install -g @google/gemini-cli
```

## 2. Kích hoạt Session đăng nhập trên Mac
Vì bạn dùng User/Pass, trên Mac bạn cần thực hiện 1 trong 2 cách sau để CLI nhận diện bạn:

### Cách 1: Login trực tiếp qua CLI (Nếu CLI hỗ trợ)
```bash
gemini login
```
Lệnh này thường sẽ mở trình duyệt, bạn nhập User/Pass Google là xong.

### Cách 2: Thủ công qua Cookies (Nếu dùng bản trích xuất SID)
Nếu CLI của bạn yêu cầu Cookie để duy trì login mà không cần API Key:
1. Mở Chrome trên Mac, đăng nhập `gemini.google.com`.
2. F12 -> Application -> Cookies.
3. Tìm giá trị `__Secure-1PSID` và `__Secure-1PSIDTS`.
4. Thêm vào file `~/.zshrc`:
   ```bash
   export GEMINI_SID="Giá_trị_copy_tại_đây"
   export GEMINI_SIDTS="Giá_trị_copy_tại_đây"
   ```
5. Chạy lệnh: `source ~/.zshrc`

## 3. Cấu hình cho Pixel Agent
Trong phần cấu hình "Create Agent" của Pixel Agent trên Mac, hãy trỏ vào file `pixel_agent_gemini_bridge.sh`.

## 4. Lưu ý quan trọng trên macOS
- **Permissions:** Mac bảo mật rất kỹ, nếu script không chạy, hãy vào `System Settings > Privacy & Security > Full Disk Access` và cấp quyền cho Terminal/iTerm2.
- **Path:** Luôn dùng `pwd` để xác định đường dẫn dự án hiện tại khi cấu hình Agent.
