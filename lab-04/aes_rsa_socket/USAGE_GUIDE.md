# 📖 HƯỚNG DẪN RUN & SỬ DỤNG - AES-RSA Socket Multi-User Chat

## 🎯 TÓM TẮT
Đây là ứng dụng **chat bảo mật** cho phép **2 hay nhiều users** trò chuyện trên **1 server** với mã hóa **AES-256 + RSA-2048**. Tất cả tin nhắn được đồng bộ real-time giữa các user.

---

# ⚙️ BƯỚC 1: CHUẨN BỊ MÔI TRƯỜNG

## 1.1 Kiểm Tra Python
Đảm bảo Python 3.7+ đã cài:
```bash
python --version    # Phải ≥ Python 3.7
```

Nếu không cài, tải từ: https://www.python.org/

## 1.2 Cài Dependencies
```bash
pip install -r requirements.txt
```

Kiểm tra cài xong:
```bash
pip list | grep Flask
pip list | grep pycryptodome
```

---

# 🚀 BƯỚC 2: KHỞI ĐỘNG SERVER

## 2.1 Chạy Ứng Dụng

**Windows:**
```bash
python run.py
```

**Linux/Mac:**
```bash
python run.py
```

## 2.2 Xác Nhận Server Chạy OK
Output sẽ hiển thị:
```
 * Running on http://127.0.0.1:5000
 * Socket Server listening on localhost:12345
 * WARNING: This is a development server. Do not use it in production.
```

✅ **Dấu hiệu thành công:**
- [ ] Đã thấy "Running on http://127.0.0.1:5000"
- [ ] Đã thấy "Socket Server listening on localhost:12345"
- [ ] Không có lỗi (error/exception)
- [ ] Terminal không bị đóng

---

# 💻 BƯỚC 3: MỞ CLIENT (BROWSER)

## 3.1 Test Single User (1 Tab)

**Mở Tab 1:** 
```
http://localhost:5000
```

🔍 **Kiểm tra giao diện:**
- [ ] Tiêu đề: "🔐 SECURE COMMUNICATION PROTOCOL"
- [ ] 2 badges: "ONLINE", "ENCRYPTION: ACTIVE" (xánh lục)
- [ ] 3 cột: Trái (Connection), Giữa (Chat), Phải (Security Info)
- [ ] Color theme: Đen background, xanh lục text

**Kết nối:**
1. Kiểm tra `SERVER HOST`: `localhost` (OK)
2. Kiểm tra `SERVER PORT`: `12345` (OK)
3. Bấm **[CONNECT]** button
4. Đợi ~1 giây

🔍 **Kiểm tra kết nối:**
- [ ] Badge: "🟢 ONLINE" (xanh)
- [ ] Badge: "🔒 ENCRYPTION: ACTIVE" (xanh)
- [ ] Message: "✓ Connected as User [xxxxxxxx]"
- [ ] Message: "🔐 AES-256 encryption active"
- [ ] Message: "🔑 RSA-2048 key exchange complete"

✅ **Nếu thấy tất cả → Single user OK**

---

## 3.2 Test Multi-User (2 Tabs) ⭐ QUAN TRỌNG

### Bước A: Mở Tab 2
```
Ctrl+T hoặc Cmd+T (mở tab mới)
Gõ: http://localhost:5000
```

### Bước B: Kết Nối Cả 2 Tabs

**Tab 1:**
- Bấm **[CONNECT]** (nếu chưa)
- Ghi nhớ User ID: `[xxxxxxxx]`
- Kiểm tra: ONLINE ✅

**Tab 2:**
- Bấm **[CONNECT]**
- Ghi nhớ User ID: `[yyyyyyyy]`
- **⭐ USER ID PHẢI KHÁC Tab 1** (rất quan trọng!)
- Kiểm tra: ONLINE ✅

### Bước C: Gửi Tin Từ Tab 1
1. Click input field (dòng chữ xám "Type encrypted message...")
2. Gõ: `Xin chào từ Tab 1`
3. Bấm **[SEND]** hoặc nhấn Enter

🔍 **Kiểm tra Tab 1:**
```
Messages area:
├─ [HH:MM:SS] YOU: Xin chào từ Tab 1
└─ Color: Xanh biển (cyanish), border xanh lục
```

🔍 **Kiểm tra Tab 2 (TỰ ĐỘNG):**
```
Messages area:
├─ [HH:MM:SS] USER_XXXXXXXX: Xin chào từ Tab 1
└─ Color: Xanh lá, border xanh lá

⭐ ĐẶC BIỆT: 
- Sender là "USER_XXXXXXXX" (ID của Tab 1), KHÔNG phải "YOU"
- Timestamp giống với Tab 1
- Message text giống hệt: "Xin chào từ Tab 1"
- Mất ~500ms để hiển thị (bình thường)
```

### Bước D: Gửi Tin Từ Tab 2
1. Tab 2: Gõ `Xin chào từ Tab 2`
2. Bấm **[SEND]**

🔍 **Kiểm tra Tab 2:**
```
Messages area:
├─ ... (tin của Tab 1)
└─ [HH:MM:SS] YOU: Xin chào từ Tab 2
   Color: Xanh biển
```

🔍 **Kiểm tra Tab 1 (TỰ ĐỘNG):**
```
Messages area:
├─ ... (tin của Tab 1)
└─ [HH:MM:SS] USER_YYYYYYYY: Xin chào từ Tab 2
   Color: Xanh lá

⭐ Tab 1 phải thấy tin từ Tab 2!
```

### ✅ Nếu cả 2 bên đều thấy tin → **MULTI-USER HOẠT ĐỘNG!** 🎉

---

# 📊 BƯỚC 4: KIỂM TRA STATISTICS

Sau khi gửi/nhận tin, kiểm tra **Right Panel (Security Info):**

```
ENCRYPTION: AES-256 CBC
KEY EXCHANGE: RSA-2048 OAEP
MESSAGES SENT: N (số tin gửi)
MESSAGES RECEIVED: M (số tin nhận)
SESSION DURATION: hh:mm:ss (thời gian kết nối)
```

🔍 **Ví dụ chuẩn:**
```
Tab 1:
├─ SENT: 1 (gửi "Xin chào từ Tab 1")
├─ RECEIVED: 1 (nhận "Xin chào từ Tab 2")

Tab 2:
├─ SENT: 1 (gửi "Xin chào từ Tab 2")
├─ RECEIVED: 1 (nhận "Xin chào từ Tab 1")
```

---

# 🔄 BƯỚC 5: CONTINUOUS TEST

Lặp lại nhiều lần:

**T1:** Gửi tin → **T2:** Nhận → Gửi tin → **T1:** Nhận ...

```
Tab 1 → "Hi"
  ↓
Tab 2 nhận "Hi" (USER_1...)
  ↓
Tab 2 → "Hello"
  ↓
Tab 1 nhận "Hello" (USER_2...)
  ↓
Tab 1 → "How are you?"
  ↓
Tab 2 nhận "How are you?" (USER_1...)
  ↓
...
```

✅ **Mục tiêu:**
- [ ] Messages sync đúng thứ tự
- [ ] Sender ID chính xác
- [ ] Không có messages bị lặp
- [ ] Timestamp chính xác
- [ ] Encryption badge luôn "ACTIVE"

---

# 🛑 BƯỚC 6: DISCONNECT (TẠM DỪNG)

Để ngắt kết nối:

**Tab 1:** Bấm **[DISCONNECT]**

🔍 **Kiểm tra:**
- [ ] Badge: "🔴 OFFLINE"
- [ ] Input field: Disabled (xám)
- [ ] Message: "Disconnected from server"

**Reconnect:**
- Bấm **[CONNECT]** lại → Kết nối lại với User ID mới

---

# 🐛 BƯỚC 7: TROUBLESHOOTING

## ❌ Lỗi: "OFFLINE" Khi Click CONNECT

**Nguyên nhân:**
- Port 12345 đang bị chiếm
- Socket server không chạy
- Firewall chặn

**Fix:**
```bash
# Terminal Mới
# 1. Kill process cũ
taskkill /PID <pid> /F

# 2. Check port
netstat -ano | findstr :12345

# 3. Khởi động lại
python run.py
```

---

## ❌ Lỗi: Message Không Sync Giữa 2 Tabs

**Nguyên nhân:**
- JavaScript lỗi
- Backend không lưu message
- Polling bị lỗi

**Fix:**
```javascript
// Mở F12 (Developer Tools) → Console

// Kiểm tra User ID
window.chatApp.userId  // Phải có value xxxxxxxx

// Kiểm tra Last Message Count
window.chatApp.lastMessageCount  // Phải tăng

// Kiểm tra Polling Interval
window.chatApp.messageUpdateInterval  // Phải có ID
```

---

## ❌ Lỗi: User ID Giống Nhau Trên 2 Tabs

**Nguyên nhân:**
- Browser cache
- Flask session không khác

**Fix:**
```bash
# 1. Xóa cookies
F12 → Application → Cookies → Delete all

# 2. Mở 2 tabs mới từ fresh
# Tab 1: localhost:5000
# Tab 2: localhost:5000 (Ctrl+T mới)
```

---

## ❌ Lỗi: Console Error "Declaration or statement expected"

**Nguyên nhân:**
- script.js bị lỗi syntax

**Fix:**
```bash
# Refresh page
F5

# Hoặc: Restart server
Ctrl+C (ngứt server)
python run.py (chạy lại)
```

---

# 📋 CHECKLIST - ALL TESTS PASSED ✅

- [ ] Server khởi động thành công (port 5000 + 12345)
- [ ] Tab 1 kết nối → ONLINE
- [ ] Tab 2 kết nối → ONLINE + User ID khác Tab 1
- [ ] Tab 1 gửi tin → Tab 2 nhận (đúng sender, timestamp, message)
- [ ] Tab 2 gửi tin → Tab 1 nhận (đúng sender, timestamp, message)
- [ ] Multiple messages: Không bị lặp, đúng thứ tự
- [ ] MESSAGES SENT/RECEIVED: Tính toán đúng
- [ ] SESSION DURATION: Tăng liên tục
- [ ] ENCRYPTION: Badge "ACTIVE", label "AES-256 CBC"
- [ ] Console (F12): Không có error messages
- [ ] All 10 checks → ✅ MULTI-USER CHAT HOẠT ĐỘNG HOÀN HẢO!

---

# 🎓 HIỂU THÊM VỀ ARCHITECTURE

## Server Architecture
```
Python run.py
    ↓
┌─────────────────────┐
│  Flask Web Server   │
│  (port 5000)        │
├─────────────────────┤
│  Routes:            │
│  /api/connect       │
│  /api/send          │
│  /api/messages      │
│  /api/disconnect    │
└─────────────────────┘
    ↓
┌─────────────────────┐
│  Socket Server      │
│  (port 12345)       │
├─────────────────────┤
│  RSA Key Exchange   │
│  AES Key Dist.      │
│  Message Relay      │
└─────────────────────┘
```

## Data Flow
```
Browser Tab 1              Browser Tab 2
    ↓                          ↓
[Session: uuid-1]      [Session: uuid-2]
    ↓                          ↓
    └────→ Flask Server ←──────┘
           (user_sockets dict)
           (messages_history list)
               ↓
          Socket Server
           (RSA + AES)
```

## Message Storage
```
messages_history = [
    {
        sender: 'USER_abc123...',  # From which user
        message: 'Hi!',
        timestamp: '10:30:45',
        encryption: 'AES-256'
    },
    {
        sender: 'USER_xyz789...',  # From different user
        message: 'Hello!',
        timestamp: '10:30:47',
        encryption: 'AES-256'
    }
]
```

---

# 🔐 BẢNG SỞ HỮU AN TOÀN

| Khía Cạnh | Chi Tiết |
|----------|---------|
| **Mã Hóa Message** | AES-256 CBC (256-bit key) |
| **Trao Đổi Khóa** | RSA-2048 OAEP (2048-bit key) |
| **IV (Initialization Vector)** | Random cho mỗi message |
| **Session ID** | UUID (Global unique) |
| **Message History** | Lưu plaintext (server-side) |
| **Transport** | HTTP (không HTTPS) |

**Ghi chú:** Dùng HTTPS được khuyên cho production!

---

# 📞 SUPPORT & CONTACT

Nếu gặp vấn đề:
1. Đọc **README.md** (Tài liệu đầy đủ)
2. Xem **TESTING_MULTIUSER.md** (Hướng dẫn chi tiết)
3. Kiểm tra **Console F12** (Lỗi JavaScript)
4. Check **Terminal** (Lỗi Python backend)

---

**Chúc bạn sử dụng Secure Chat vui vẻ! 🎉🔐**

Mọi câu hỏi → Đọc file `README.md`
