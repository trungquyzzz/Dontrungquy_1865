# 👋 START HERE - Đọc File Này Trước!

Chào mừng đến với **Secure Chat** - Ứng dụng chat bảo mật sử dụng AES-256 & RSA-2048! 🔐

---

## ⚡ 5 Giây Nhanh Nhất

```bash
pip install -r requirements.txt  # Cài dependencies
python run.py                    # Chạy ứng dụng
# Mở browser → http://localhost:5000
```

**Xong!** 🎉

---

## 📚 Hướng Dẫn Đọc File (Theo Thứ Tự)

### 0️⃣ **QUICK_REFERENCE.md** (2 phút) ← 👈 ĐỌC ĐÃ!
   - Commands & shortcuts cheatsheet
   - API endpoints
   - Common workflows

### 1️⃣ **USAGE_GUIDE.md** (5 phút) ← 👈 CHÍNH ĐỒNG
   - Bước-by-bước chạy ứng dụng
   - Test single & multi-user
   - Troubleshooting
   
### 2️⃣ **SUMMARY.md** (5 phút)
   - Tổng quan project
   - Tính năng chính
   - Cách hoạt động cơ bản

### 3️⃣ **TESTING_MULTIUSER.md** (Chi tiết)
   - Test procedures ngắn
   - Debug checking
   - Performance metrics

### 4️⃣ **README.md** (15 phút) ← **Đọc Cẩn Thận**
   - Tài liệu đầy đủ
   - Cài đặt chi tiết
   - Cách sử dụng
   - Bảo mật giải thích
   - Troubleshooting

### 5️⃣ **SETUP_GUIDE.md** (Nếu gặp vấn đề)
   - Cài đặt từng OS
   - Firewall config
   - Production setup

### 6️⃣ **DESIGN.md** (Nếu muốn customize)
   - Thiết kế giao diện
   - Color palette
   - Component details

### 7️⃣ **INDEX.md** (Tham khảo)
   - Danh mục tất cả file
   - Giải thích chi tiết code

---

## 🎯 Nhanh Chóng Bắt Đầu

### For Người Mới
```
1. Đọc USAGE_GUIDE.md (5 min)
   ↓
2. Chạy: python run.py
   ↓
3. Mở: http://localhost:5000 (2 tabs)
   ↓
4. CONNECT cả 2 tabs ✅
   ↓
5. Test: Tab 1 gửi → Tab 2 nhận ✅
```

### For Người Có Kinh Nghiệm
```
1. Xem QUICK_REFERENCE.md (commands)
   ↓
2. Xem README.md → Bảo mật section
   ↓
3. Xem code: web_server.py, server.py
   ↓
4. Customize: style.css, config ports
   ↓
5. Deploy: SETUP_GUIDE.md → Production
```

---

## ❓ Tôi Muốn Làm Gì?

| Mục Đích | Đọc File | Thời Gian |
|----------|----------|----------|
| **Chạy ngay** | USAGE_GUIDE.md | 5 min |
| **Quick commands** | QUICK_REFERENCE.md | 2 min |
| **Test multi-user** | TESTING_MULTIUSER.md | 10 min |
| **Hiểu cơ bản** | SUMMARY.md | 5 min |
| **Cài đặt đầy đủ** | README.md | 15 min |
| **Fix lỗi** | SETUP_GUIDE.md | 10 min |
| **Thay đổi giao diện** | DESIGN.md | 10 min |
| **Tìm file cụ thể** | INDEX.md | 5 min |

---

## 📦 Yêu Cầu Trước

✅ Python 3.7+
✅ Pip (Python package manager)
✅ Browser (Chrome, Firefox, Edge)
✅ ~100 MB disk space

---

## 🚀 Step-by-Step Chạy Lần Đầu

### Step 1: Mở Terminal/CMD
```bash
# Windows
# Nhấn: Win + R → cmd → Enter

# Linux/Mac
# Nhấn: Ctrl + Alt + T (hoặc mở Terminal)
```

### Step 2: Chuyển Thư Mục
```bash
cd "C:\Users\Mr Quy\Downloads\Dontrungquy_1865\Dontrungquy_1865\lab-04\aes_rsa_socket"
# (Thay đường dẫn nếu cần)
```

### Step 3: Cài Dependencies
```bash
pip install -r requirements.txt
```
Sẽ cài: Flask, PyCryptodome, Flask-CORS, v.v.

### Step 4: Chạy Ứng Dụng
```bash
# Windows
run.bat

# Hoặc
python run.py

# Linux/Mac
python run.py
```

### Step 5: Mở Browser
```
Truy cập: http://localhost:5000
```

### Step 6: Chat!
```
1. Host: localhost
2. Port: 12345
3. Click: CONNECT
4. Nhập tin nhắn → SEND ✅
```

---

## ✅ Dấu Hiệu Chạy Thành Công

### Terminal Output
```
[1/3] Checking dependencies...
✓ Dependencies are installed

[2/3] Starting Socket Server...
✓ Socket Server started

[3/3] Starting Flask Web Server...
✓ SECURE CHAT is running!

📱 Open your browser and go to: http://localhost:5000
```

### Browser Screen
```
✓ Header shows "🔐 SECURE COMMUNICATION PROTOCOL"
✓ Right panel shows encryption info
✓ Input field is active (không disabled)
✓ Status indicator visible
```

---

## 🎨 Giao Diện Trông Như Thế Nào

**Dark Theme với Neon Colors:**
- 🟢 Neon Green (#00ff41) - Primary
- 🔵 Sky Blue (#0099ff) - Secondary
- ⚫ Deep Black (#050810) - Background
- Terminal-like appearance
- Hacker aesthetic

Xem **DESIGN.md** để biết chi tiết.

---

## 🔐 Bảo Mật Được Giải Thích

```
User Type Message
↓
AES-256 Encrypt (256-bit key)
↓
Send via Socket
↓
Server Receive
↓
AES-256 Decrypt
↓
Display Message

Key Exchange:
RSA-2048 OAEP → Generate AES-256 key safely
```

Xem **README.md** → "Bảo Mật" section để hiểu rõ.

---

## 📁 Cấu Trúc Thư Mục

```
aes_rsa_socket/
├── START_HERE.md       ← Bạn đang đọc
├── SUMMARY.md          ← Tổng quan
├── QUICK_START.md      ← Khởi động nhanh
├── README.md           ← Tài liệu đầy đủ ⭐
├── SETUP_GUIDE.md      ← Setup chi tiết
├── DESIGN.md           ← Thiết kế UI
├── INDEX.md            ← Danh mục file
│
├── run.py              ← Chạy ứng dụng 🚀
├── run.bat             ← Batch Windows
│
├── web_server.py       ← Flask server
├── server.py           ← Socket server
├── client.py           ← Client reference
├── requirements.txt    ← Dependencies
│
├── templates/
│   └── chat.html       ← HTML giao diện
│
└── static/
    ├── style.css       ← CSS styling
    └── script.js       ← JavaScript logic
```

---

## 🆘 Gặp Vấn Đề?

### ❌ "Port already in use"
→ Xem **SETUP_GUIDE.md** → "Khắc Phục Sự Cố"

### ❌ "Module not found"
```bash
pip install -r requirements.txt
```

### ❌ "Connection refused"
→ Xem **QUICK_START.md** → "Troubleshooting"

### ❌ Khác
→ Xem **README.md** → "Khắc Phục Sự Cố"

---

## 💡 Tips

1. **Nếu bạn bận**: Xem QUICK_START.md (2 phút)
2. **Nếu bạn có thời gian**: Đọc README.md (15 phút)
3. **Nếu bạn gặp lỗi**: Xem SETUP_GUIDE.md
4. **Nếu bạn muốn hiểu**: Đọc tất cả files!

---

## 📞 Hỗ Trợ

| Câu Hỏi | Tìm Đáp Án |
|--------|----------|
| Cách chạy? | QUICK_START.md |
| Là gì, làm gì? | SUMMARY.md |
| Chi tiết? | README.md |
| Lỗi setup? | SETUP_GUIDE.md |
| Thay đổi giao diện? | DESIGN.md |
| File nào làm gì? | INDEX.md |

---

## 🎓 Bạn Sẽ Học Được

✅ Mã hóa AES-256
✅ Trao đổi khóa RSA-2048
✅ Socket programming
✅ Flask framework
✅ Web development
✅ Real-time communication
✅ Security best practices

---

## 🏁 Bước Tiếp Theo

```
1️⃣ Đọc SUMMARY.md (5 min)
   ↓
2️⃣ Chạy: python run.py
   ↓
3️⃣ Mở: http://localhost:5000
   ↓
4️⃣ Chat!
```

---

## 🎉 Ready to Go!

```
👉 Bạn có 2 lựa chọn:

✅ Cách 1 - Nhanh (5 phút)
   1. python run.py
   2. http://localhost:5000
   3. Copy lệnh này: run.bat (Windows)

✅ Cách 2 - Chi tiết (30 phút)
   1. Đọc SUMMARY.md
   2. Đọc README.md
   3. Chạy ứng dụng
   4. Explore code
```

---

## 🚀 Giờ Hãy Bắt Đầu!

```bash
# Copy-paste lệnh này để chạy:
python run.py

# Hoặc Windows:
run.bat
```

**Browser sẽ mở tự động → http://localhost:5000**

---

## 📚 Tệp Tiếp Theo Đọc

👉 **Tiếp theo**: Mở **SUMMARY.md** hoặc **QUICK_START.md**

---

**Have fun! 🎉🔐**

*Gợi ý: Lưu link này để quay lại!*

---

### Bạn có câu hỏi gì?

- **Cách chạy?** → QUICK_START.md
- **Hiểu chi tiết?** → README.md  
- **Troubleshoot?** → SETUP_GUIDE.md
- **Customize?** → DESIGN.md

**← Quay lại START_HERE.md lúc cần!**
