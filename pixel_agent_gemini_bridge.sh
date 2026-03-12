#!/bin/bash

# BRIDGE CHO PIXEL AGENT TRÊN MAC (PHIÊN BẢN USER LOGIN)

# 1. Kiểm tra session hiện có (Giả định CLI lưu session vào file/cookie)
# Nếu CLI của bạn có lệnh 'check status' hãy dùng nó.
# Ở đây ta mặc định là CLI sẽ tự dùng session login cũ.

# 2. Nếu chưa login, hãy login thủ công qua browser 1 lần duy nhất:
# gemini login

# 3. Cấu hình System Prompt dự án Luật Sư
SYSTEM_PROMPT="Bạn là Senior Developer. Nhiệm vụ: Phát triển App Luật Sư.
Dữ liệu: AppLuatSu/Resources/questions_data.json.
Cách làm: Research -> Strategy -> Execution.
Tuân thủ GEMINI.md."

# 4. Khi Pixel Agent bấm 'Create Agent', nó sẽ thực thi dòng lệnh này:
# Lưu ý: --session-mode là tham số giả định cho việc dùng user login (không API Key)
gemini --system "$SYSTEM_PROMPT" --context ./GEMINI.md
