# 📑 FILE INDEX - Secure Chat Project

Danh sách chi tiết tất cả các file trong project Secure Chat AES-RSA.

---

## 🗂️ Cấu Trúc Thư Mục

```
aes_rsa_socket/
├── 📄 File Chính
│   ├── run.py                    ⭐ Script chạy ứng dụng (khuyên dùng)
│   ├── run.bat                   ⭐ Batch file cho Windows
│   ├── web_server.py             Flask server + Socket API handler
│   ├── server.py                 Socket server gốc
│   ├── client.py                 Client socket (reference)
│   └── requirements.txt           Danh sách dependencies
│
├── 📚 Tài Liệu
│   ├── README.md                 🔴 Tài liệu đầy đủ (đọc trước)
│   ├── QUICK_START.md            ⚡ Hướng dẫn nhanh (2 phút)
│   ├── SETUP_GUIDE.md            🔧 Hướng dẫn cài đặt chi tiết
│   └── INDEX.md                  📑 File này (danh sách file)
│
├── 📁 templates/
│   └── chat.html                 HTML giao diện chat
│
├── 📁 static/
│   ├── style.css                 CSS styling (hacker theme)
│   └── script.js                 JavaScript logic & event handlers
│
├── 🔑 keys/
│   └── (Empty - lưu RSA keys)
│
└── 📋 Khác
    └── (Tự động tạo: __pycache__, .venv, etc.)
```

---

## 📄 CHI TIẾT TỪ FILE RFI

### 🔴 README.md
**Loại**: Tài liệu
**Ngôn ngữ**: Markdown
**Đọc trước**: ✅ Bắt buộc
**Nội dung**:
- Giới thiệu project
- Tính năng chính
- Yêu cầu hệ thống
- Cài đặt bước-theo-bước
- Cách sử dụng chi tiết
- Giải thích bảo mật
- Khắc phục sự cố
- Tài liệu tham khảo

**Khi đọc**: Lần đầu tiên setup project

---

### ⚡ QUICK_START.md
**Loại**: Hướng dẫn nhanh
**Ngôn ngữ**: Markdown
**Thời gian**: ~2 phút
**Nội dung**:
- Khởi động nhanh
- Lệnh cơ bản
- Cấu hình tùy chỉnh
- Khắc phục sự cố nhanh
- Mẹo sử dụng
- Hỗ trợ

**Khi đọc**: Sau khi cài đặt xong

---

### 🔧 SETUP_GUIDE.md
**Loại**: Hướng dẫn chi tiết
**Ngôn ngữ**: Markdown
**Nội dung**:
- Setup Windows 10/11
- Setup Linux (Ubuntu)
- Setup macOS
- Chạy trên Network
- Firewall configuration
- Testing guide
- Configuration options
- Production setup
- Debugging

**Khi đọc**: Nếu gặp vấn đề cài đặt

---

### ⭐ run.py
**Loại**: Python Script
**Chức năng**: Chạy ứng dụng hoàn chỉnh
**Usage**:
```bash
python run.py
```

**Tính năng**:
- Kiểm tra Python version
- Kiểm tra dependencies
- Khởi động Socket Server
- Khởi động Flask Web Server
- Xử lý Ctrl+C gracefully
- Hiển thị thông tin khởi động

**Khuyên**: ✅ Sử dụng cách này để chạy

---

### ⭐ run.bat
**Loại**: Batch Script (Windows)
**Chức năng**: Chạy ứng dụng trên Windows
**Usage**:
- Double-click file, hoặc
- `run.bat` trong Command Prompt

**Advantage**: Dễ dùng nhất cho Windows users

---

### 🔌 web_server.py
**Loại**: Python Flask Application
**Dòng code**: ~200
**Chức năng**:
- Phục vụ giao diện HTML
- Quản lý kết nối socket
- Mã hóa/Giải mã messages
- API endpoints

**Classes**:
```python
class SocketManager:
    - connect_to_server()    # Kết nối đến server
    - encrypt_message()      # Mã hóa AES
    - decrypt_message()      # Giải mã AES
    - send_message()         # Gửi tin nhắn
    - receive_message()      # Nhận tin nhắn
    - disconnect()           # Ngắt kết nối
```

**Routes**:
- `GET /`                   → Hiển thị chat.html
- `POST /api/connect`       → Kết nối server
- `POST /api/send`          → Gửi tin nhắn
- `GET /api/messages`       → Lấy lịch sử
- `GET /api/status`         → Trạng thái kết nối
- `POST /api/disconnect`    → Ngắt kết nối

**Configuration**:
```python
Host: 0.0.0.0
Port: 5000
Debug: True
```

**When Modified**: Nếu cần đổi port, logic mã hóa, hoặc API

---

### 🖥️ server.py
**Loại**: Python Socket Server
**Dòng code**: ~70
**Chức năng**: Socket server mã hóa AES-RSA

**Features**:
- Listen on port 12345
- Generate RSA-2048 key pair
- Handle multiple clients
- AES-256 CBC encryption
- Message broadcasting

**Functions**:
```python
encrypt_message(key, message)    # Mã hóa
decrypt_message(key, encrypted)  # Giải mã
handle_client(socket, address)   # Xử lý client
```

**When Running**: Tự động chạy khi `python run.py`

---

### 💬 client.py
**Loại**: Python Socket Client (Reference)
**Dòng code**: ~50
**Chức năng**: Client socket cơ bản (dùng để reference)

**Note**: Không cần chạy trực tiếp
- Web server (`web_server.py`) là client chính

---

### 📦 requirements.txt
**Loại**: Python Dependencies List
**Nội dung**:
```
pycryptodome==3.18.0    # Mã hóa AES/RSA
Flask==2.3.2            # Web framework
python-socketio==5.9.0  # Socket.IO (optional)
python-engineio==4.7.1  # Engine.IO (optional)
flask-cors==4.0.0       # CORS support
```

**Install**:
```bash
pip install -r requirements.txt
```

---

### 🎨 chat.html
**Loại**: HTML5 Template
**Dòng code**: ~150
**Chức năng**: Giao diện chat chính

**Structure**:
```html
<header>           → Tiêu đề + Status
<main>
  ├── Connection Panel   → Setup host/port
  ├── Chat Area          → Messages + Input
  └── Security Panel     → Info bảo mật
<footer>           → Warnings + Copyright
```

**Features**:
- Responsive design
- Real-time message updates
- Status indicators
- Security information display

**Modified by**: Flask template engine (Jinja2)

---

### 🎨 style.css
**Loại**: CSS3 Stylesheet
**Dòng code**: ~600
**Chức năng**: Styling giao diện theo phong cách hacker

**Theme Colors**:
- Primary: `#00ff41` (Neon Green)
- Secondary: `#0099ff` (Sky Blue)
- Danger: `#ff006e` (Pink Red)
- Background: `#050810` (Deep Black)

**Sections**:
- `:root` → CSS variables (colors, fonts)
- `body` → Global styling
- `.header` → Top bar
- `.chat-container` → Main layout (3-column grid)
- `.messages-container` → Message display
- `.input-area` → Message input
- `.panel-title`, `.btn`, `.message` → Components
- `@media` → Responsive design
- `@keyframes` → Animations (pulse, glow, slideIn)

**Key Features**:
- Dark theme (hacker style)
- Glowing effects
- Terminal-like appearance
- Smooth animations
- Scrollbar customization

---

### 📝 script.js
**Loại**: JavaScript (Vanilla)
**Dòng code**: ~350
**Chức năng**: Client-side logic

**Class**:
```javascript
class SecureChatApp {
    // Methods:
    - connect()              // Kết nối server
    - disconnect()           // Ngắt kết nối
    - sendMessage()          // Gửi tin nhắn
    - fetchMessages()        // Lấy messages
    - addUserMessage()       // Thêm user message
    - addServerMessage()     // Thêm server message
    - addSystemMessage()     // Thêm system message
    - updateConnectionStatus() // Update status
    - updateEncryptionStatus() // Update encryption
    - startSessionTimer()     // Timer cho session
    - getTimestamp()         // Format thời gian
    - escapeHtml()          // Escape HTML
}
```

**Features**:
- RESTful API calls
- Real-time message polling
- DOM manipulation
- Event listeners
- Timestamp management
- Message history

**AJAX Endpoints**:
- `/api/connect` (POST)
- `/api/send` (POST)
- `/api/messages` (GET)
- `/api/status` (GET)
- `/api/disconnect` (POST)

---

## 🔄 Data Flow Diagram

```
┌─────────────────────────────────────────────────────────┐
│                    User Browser                         │
│  ┌────────────────────────────────────────────────────┐ │
│  │           chat.html (UI)                           │ │
│  │      ↓          ↓           ↓                       │ │
│  │    style.css  script.js   Flask Routes             │ │
│  └────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
              ↓ (HTTP/AJAX)
┌─────────────────────────────────────────────────────────┐
│        Flask Web Server (web_server.py)                 │
│      ┌─────────────────────────────────────┐            │
│      │     SocketManager Class              │            │
│      │  (AES Encrypt/Decrypt Logic)        │            │
│      └─────────────────────────────────────┘            │
└─────────────────────────────────────────────────────────┘
              ↓ (Socket)
┌─────────────────────────────────────────────────────────┐
│        Socket Server (server.py)                        │
│      Port 12345, RSA-2048, AES-256                      │
└─────────────────────────────────────────────────────────┘
```

---

## 📊 File Size Reference

| File | Size | Lines |
|------|------|-------|
| web_server.py | ~8 KB | 220 |
| server.py | ~2 KB | 70 |
| chat.html | ~6 KB | 150 |
| style.css | ~18 KB | 600 |
| script.js | ~12 KB | 350 |
| README.md | ~12 KB | 400 |
| QUICK_START.md | ~8 KB | 300 |
| SETUP_GUIDE.md | ~15 KB | 500 |
| **Total** | **~81 KB** | **~2500** |

---

## 🔐 Security Files

### Mã Hóa Logic
- **File**: `web_server.py` + `server.py`
- **Method**: AES-256 CBC (web_server.py) + RSA-2048 OAEP (server.py)
- **Key Exchange**: RSA-2048 OAEP
- **IV**: Random per message

### Certificate/Keys
- **Location**: `keys/` folder
- **Generated**: At runtime
- **Type**: RSA public/private key pairs

---

## 🚀 Execution Order

Khi chạy `python run.py`:

1. **run.py** starts
   - Check Python version
   - Check dependencies
   - Start server.py (background)
   - Start web_server.py (foreground)

2. **server.py**
   - Bind to localhost:12345
   - Generate RSA-2048 keys
   - Listen for connections

3. **web_server.py**
   - Load Flask app
   - Load templates & static files
   - Bind to 0.0.0.0:5000
   - Running on http://127.0.0.1:5000

4. **User**
   - Opens http://localhost:5000
   - Loads chat.html (via Flask)
   - Loads style.css, script.js
   - Inputs host/port
   - Clicks CONNECT
   - JavaScript calls `/api/connect`
   - Flask connects to server socket
   - Begin encrypted chat

---

## 📝 Modification Guide

### Bạn muốn...

**Đổi màu giao diện?**
→ Sửa `style.css` → `:root` section

**Đổi port?**
→ Sửa `server.py` (12345) hoặc `web_server.py` (5000)

**Thêm database?**
→ Sửa `web_server.py` → add SQLAlchemy

**Thêm user authentication?**
→ Sửa `web_server.py` + `chat.html`

**Đổi mã hóa algorithm?**
→ Sửa `encrypt_message()` + `decrypt_message()` functions

**Thêm file sharing?**
→ Thêm multer + binary handling

---

## ✅ File Checklist Sebelum Deploy

- [ ] `requirements.txt` updated
- [ ] `web_server.py` production settings
- [ ] `server.py` bind correct host/port
- [ ] `chat.html` no debug statements
- [ ] `script.js` API endpoints correct
- [ ] `style.css` responsive tested
- [ ] All dependencies installed
- [ ] Ports not conflicting
- [ ] Firewall rules configured
- [ ] Logging enabled
- [ ] Error handling implemented

---

## 🎓 Learning Path

**Newbie:**
1. Đọc `QUICK_START.md`
2. Chạy `python run.py`
3. Sử dụng giao diện

**Intermediate:**
1. Đọc `README.md`
2. Xem `web_server.py`
3. Hiểu AES/RSA logic
4. Modify `style.css`

**Advanced:**
1. Đọc `SETUP_GUIDE.md`
2. Xem `server.py`
3. Implement firewall
4. Production deployment
5. Add features

---

**Happy Coding! 🚀🔐**

Nếu có thắc mắc, xem README.md hoặc SETUP_GUIDE.md
