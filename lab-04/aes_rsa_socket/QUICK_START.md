# ⚡ QUICK START - Secure Chat

## 🚀 Khởi động nhanh chóng (2 phút)

### Bước 1: Kiểm tra yêu cầu
Đảm bảo bạn đã cài Python 3.7+ tại đây: https://www.python.org/

```bash
python --version
```

### Bước 2: Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### Bước 3: Chạy ứng dụng

#### Windows:
```bash
run.bat
```

Hoặc:
```bash
python run.py
```

#### Linux/Mac:
```bash
python run.py
```

### Bước 4: Mở browser
Truy cập: **http://localhost:5000**

### Bước 5: Kết nối và chat
1. Mặc định Host: `localhost`, Port: `12345`
2. Bấm **CONNECT**
3. Bắt đầu chat! 💬🔐

---

## 📋 Cấu Hình Tùy Chỉnh

### Thay đổi Port Socket Server
Sửa trong `server.py`:
```python
server_socket.bind(('localhost', 12345))  # Thay 12345 thành port khác
```

### Thay đổi Port Web Server
Sửa cuối cùng của `web_server.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Thay 5000 thành port khác
```

### Cho phép truy cập từ máy khác
Sửa dalam `web_server.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # 0.0.0.0 cho phép tất cả
```

Rồi từ máy khác nhập: `http://<ip-của-máy>:5000`

---

## 🔧 Khắc Phục Sự Cố

### Lỗi: "Address already in use"
Port đã được sử dụng. Chọn port khác hoặc:

**Windows:**
```bash
netstat -ano | findstr :12345
taskkill /PID <PID> /F
```

**Linux/Mac:**
```bash
lsof -i :12345
kill -9 <PID>
```

### Lỗi: "ModuleNotFoundError"
Cài dependencies:
```bash
pip install -r requirements.txt
```

### Giao diện không tải được
- Refresh trang (F5)
- Xóa cache browser (Ctrl+Shift+Delete)
- Kiểm tra Console (F12) để tìm lỗi

---

## 📊 Cấu Trúc Thư Mục

```
aes_rsa_socket/
├── run.py              ⭐ Script chạy ứng dụng
├── run.bat             ⭐ Batch file cho Windows
├── web_server.py       Flask server + Socket handler
├── server.py           Socket server gốc
├── client.py           Client socket (để tham khảo)
├── requirements.txt    Dependencies
├── README.md           Tài liệu đầy đủ
├── QUICK_START.md      File này
├── templates/
│   └── chat.html       HTML giao diện chat
├── static/
│   ├── style.css       Styling CSS (hacker theme)
│   └── script.js       JavaScript logic
└── keys/               Lưu trữ RSA keys
```

---

## 🎯 Tính Năng Chính

✅ **AES-256 Encryption** - Mã hóa mạnh mẽ
✅ **RSA-2048 Key Exchange** - Trao đổi khóa an toàn
✅ **Real-time Chat** - Chat trực tiếp
✅ **Hacker Design** - Giao diện chuyên nghiệp
✅ **Security Info** - Theo dõi trạng thái bảo mật
✅ **Session Tracking** - Thống kê phiên kết nối

---

## 💡 Tips

1. **Chạy trên cùng máy**: Mặc định localhost:12345 ✅
2. **Chạy trên máy khác**: 
   - Server: Một máy
   - Client Web: Máy khác
   - Nhập Host là IP của server

3. **Firewall**: Nếu kết nối thất bại, kiểm tra firewall
4. **Development Mode**: Flask sẽ auto-reload khi code thay đổi

---

## 🔐 Bảo Mật

- Tất cả tin nhắn được mã hóa AES-256 CBC
- Khóa AES được trao đổi an toàn qua RSA-2048 OAEP
- Mỗi tin nhắn có IV ngẫu nhiên
- So sánh hash để xác minh tính toàn vẹn (optional)

---

## 📝 Ví Dụ Sử Dụng

```
Máy A (Server):                  Máy B (Client):
python run.py         -------->  http://maquaA:5000
[Socket Server OK]               [Kết nối đến]
[Web Server OK]                  [Nhập Host: maquaA]
[Waiting...]                     [Port: 12345]
                                 [Bấm CONNECT]
[Client Connected]  <----------  [Connected!]
[Encryption OK]                  [Encryption OK]
                                 [Chat...] ----->
[Message received]   <-----------[...]
[Encrypted]                      [...]
```

---

## 🎨 Giao Diện Tổng Quan

```
┌────────────────────────────────────────────────────────────┐
│ 🔐 SECURE COMMUNICATION PROTOCOL        🟢 ONLINE ACTIVE   │
├────┬──────────────────────────────────────────────┬────────┤
│    │                                              │        │
│ ⚙️  │          💬 CHAT MESSAGES                   │ 🛡️   │
│    │                                              │        │
│ Conn│ [10:30:45] YOU: Hello                      │ Enc: AES│
│ Sett│ [10:30:47] SERVER: Hi there!              │ Key: RSA│
│    │                                              │ Sent: 5 │
│────┤ ┌───────────────────────────────────────┐  │ Recv: 3 │
│    │ │ Type message...          [📤 SEND]     │  │ Time:   │
│ Con│ └───────────────────────────────────────┘  │ 00:05:32│
│ Disc│ 🔒 Encryption active                      │        │
└────┴──────────────────────────────────────────────┴────────┘
│ ⚠️ Do not share sensitive credentials during communication  │
└────────────────────────────────────────────────────────────┘
```

---

## 📞 Hỗ Trợ

Nếu gặp vấn đề:
1. Đọc README.md (tài liệu đầy đủ)
2. Kiểm tra Console/Terminal cho lỗi
3. Thử Refresh page và reconnect
4. Xóa cache & cookies browser

---

**Chúc bạn sử dụng Secure Chat vui vẻ! 🎉🔐**
