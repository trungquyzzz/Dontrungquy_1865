# 🔐 Secure Chat - AES-RSA Encrypted Communication

Một giao diện chat chuyên nghiệp theo phong cách bảo mật của hacker, sử dụng mã hóa AES-256 và RSA-2048 để giao tiếp an toàn.

## 🎯 Tính Năng

- **Mã hóa AES-256 CBC**: Mã hóa tất cả các tin nhắn
- **Trao đổi khóa RSA-2048 OAEP**: Bảo vệ khóa AES trong quá trình truyền
- **Giao diện Hacker Style**: Thiết kế tối cực với hiệu ứng neon
- **Thời gian thực**: Chat trực tiếp với server
- **Theo dõi Bảo mật**: Thông tin chi tiết về trạng thái mã hóa
- **Lịch sử Phiên**: Theo dõi thời lượng kết nối và số lượng tin nhắn

## 📋 Yêu Cầu

- Python 3.7+
- virtualenv hoặc venv

## ⚙️ Cài Đặt

### 1. Cài đặt Dependencies

```bash
pip install -r requirements.txt
```

### 2. Khởi động Server (Nếu chạy socket server riêng)

```bash
python server.py
```

### 3. Khởi động Web Server

```bash
python web_server.py
```

Server sẽ chạy tại: `http://localhost:5000`

## 🚀 Cách Sử Dụng

### Bước 1: Mở Giao Diện
Truy cập vào trình duyệt và vào địa chỉ:
```
http://localhost:5000
```

### Bước 2: Cấu Hình Kết Nối
1. Nhập **Server Host**: `localhost` (hoặc IP của server)
2. Nhập **Server Port**: `12345` (hoặc cổng của server)

### Bước 3: Kết Nối Bảo Mật
1. Bấm nút **CONNECT** 
2. Hệ thống sẽ:
   - Tạo cặp khóa RSA-2048 (client)
   - Trao đổi khóa RSA với server
   - Tạo khóa AES-256 cho phiên
   - Thiết lập kênh mã hóa

### Bước 4: Gửi Tin Nhắn
1. Nhập tin nhắn vào ô input
2. Bấm nút **SEND** hoặc nhấn **Enter**
3. Tin nhắn sẽ được mã hóa AES-256 trước khi gửi

### Bước 5: Ngắt Kết Nối
Bấm nút **DISCONNECT** khi hoàn thành

## 🔐 Bảo Mật

### Quá trình Mã hóa:

```
┌─────────────────┐
│   Client App    │
└────────┬────────┘
         │ Tin nhắn gốc
         ▼
┌─────────────────────────────┐
│ Mã hóa AES-256 CBC          │
│ - Chế độ: CBC (Block)       │
│ - Key: 256-bit              │
│ - IV: Random (mỗi tin)      │
└────────┬────────────────────┘
         │ Tin nhắn mã hóa
         ▼
┌─────────────────────────────┐
│ Gửi qua Socket              │
└────────┬────────────────────┘
         │ Dữ liệu mã hóa
         ▼
┌─────────────────┐
│   Server Socket │
└─────────────────┘
```

### Trao đổi Khóa:

```
Client                              Server
│                                   │
├─ Tạo cặp khóa RSA-2048 ───────────┤
│                                   ├─ Tạo cặp khóa RSA-2048
├─ Nhận Public Key Server ◀─────────┤
│                                   │
├─ Gửi Public Key Client ───────────►
│                                   ├─ Nhận Public Key Client
│                                   ├─ Tạo khóa AES-256
├─ Nhận AES Key (mã hóa RSA) ◀─────┤
│                                   ├─ Mã hóa AES-256 bằng
├─ Giải mã AES-256                 │   Public Key Client
│  bằng Private Key                │   (RSA-2048 OAEP)
│                                   │
└─ Kênh mã hóa AES sẵn sàng ────────┘
```

## 📊 Giao Diện

### Thành Phần Chính:

1. **Header (Top)**
   - Tiêu đề: SECURE COMMUNICATION PROTOCOL
   - Tình trạng kết nối (Online/Offline)
   - Trạng thái mã hóa

2. **Left Panel - Connection Settings**
   - Cấu hình Host và Port
   - Nút Connect/Disconnect

3. **Center - Chat Area**
   - Hiển thị lịch sử tin nhắn
   - Ô nhập tin nhắn
   - Hiển thị trạng thái mã hóa

4. **Right Panel - Security Info**
   - Thông tin mã hóa (AES-256, RSA-2048)
   - Số tin nhắn gửi/nhận
   - Thời lượng phiên

5. **Footer (Bottom)**
   - Cảnh báo bảo mật
   - Thông tin bản quyền

## 🎨 Phong Cách Thiết Kế

- **Màu Chủ Đạo**: Xanh neon (#00ff41)
- **Màu Phụ**: Xanh dương (#0099ff)
- **Nền**: Đen sâu (#050810)
- **Font**: Courier New (Terminal style)
- **Hiệu Ứng**: Glow, pulse, slide-in animations
- **Bố Cục**: Grid responsive

## 📝 Các File

```
aes_rsa_socket/
├── web_server.py          # Flask server chính
├── server.py              # Socket server gốc
├── client.py              # Client socket gốc
├── requirements.txt       # Dependencies
├── templates/
│   └── chat.html          # Giao diện HTML
├── static/
│   ├── style.css          # Styling CSS
│   └── script.js          # Logic JavaScript
└── README.md              # File này

keys/
```

## 🔧 Cấu Hình

### Flask Settings (web_server.py)
```python
Host: 0.0.0.0
Port: 5000
Debug: True
```

### Socket Settings
```python
Server Host: localhost
Server Port: 12345
RSA Key Size: 2048 bit
AES Key Size: 256 bit (32 bytes)
AES Mode: CBC
```

## 🐛 Khắc Phục Sự Cố

### Không kết nối được đến server
- Kiểm tra server socket đang chạy: `python server.py`
- Kiểm tra Host và Port có đúng không
- Kiểm tra Firewall

### Tin nhắn không được nhận
- Kiểm tra kết nối trong "Status" (phải là ONLINE)
- Kiểm tra Server có đang chạy không
- Xem Console của Server để tìm lỗi

### Lỗi Mã hóa/Giải mã
- Refresh trang web
- Disconnect và Connect lại
- Kiểm tra console browser (F12) để tìm lỗi

## 📚 Tài Liệu Tham Khảo

- **PyCryptodome**: https://pycryptodome.readthedocs.io/
- **Flask**: https://flask.palletsprojects.com/
- **AES Encryption**: https://en.wikipedia.org/wiki/Advanced_Encryption_Standard
- **RSA Encryption**: https://en.wikipedia.org/wiki/RSA_(cryptosystem)

## ⚠️ Lưu Ý Bảo Mật

- Đây là mục đích **giáo dục/demo**
- Không sử dụng trong production mà không xem xét an ninh kỹ lưỡng
- Luôn cập nhật các thư viện mã hóa
- Không chia sẻ private key
- Sử dụng HTTPS trong production

## 👨‍💻 Tác Giả

Xây dựng cho mục đích học tập và hiểu rõ hơn về mã hóa AES-RSA

## 📄 Giấy Phép

Miễn phí sử dụng cho mục đích giáo dục
