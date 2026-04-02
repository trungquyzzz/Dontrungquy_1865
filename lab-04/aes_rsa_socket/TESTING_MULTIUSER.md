# 🧪 TESTING MULTI-USER CHAT - Hướng Dẫn Chi Tiết

## ✅ Chuẩn Bị Trước

### Bước 1: Cài Dependencies
```bash
pip install -r requirements.txt
```

Kiểm tra các package cần thiết:
- Flask 2.3.2
- PyCryptodome
- python-socketio
- python-engineio
- Flask-CORS

### Bước 2: Khởi Động Server
```bash
python run.py
```

Bạn sẽ thấy output:
```
 * Running on http://127.0.0.1:5000
 * Socket Server listening on localhost:12345
```

✅ **Dấu hiệu thành công:** Không có error messages

---

## 🎯 TEST MULTI-USER CHAT (2 USERS)

### Test 1: Cơ Bản - 2 Tabs Trên 1 Máy

**Bước 1: Mở 2 Tabs**
- Tab 1: `http://localhost:5000` 
- Tab 2: `http://localhost:5000`

**Bước 2: Kết Nối Tab 1**
```
Giao diện Tab 1:
├─ SERVER HOST: localhost (mặc định)
├─ SERVER PORT: 12345 (mặc định)
└─ [CONNECT] button

Bấm: CONNECT
```

🔍 **Kiểm tra Tab 1:**
```
Header badge: 🟢 ONLINE ✅
Status badge: 🔒 ENCRYPTION: ACTIVE ✅
Tin nhắn: ✓ Connected as User [xxxxxxxx] ✅
         🔐 AES-256 encryption active
         🔑 RSA-2048 key exchange complete
```

**Bước 3: Kết Nối Tab 2**
```
Lặp lại bước 2 trên Tab 2
```

🔍 **Kiểm tra Tab 2:**
```
Header badge: 🟢 ONLINE ✅
Status badge: 🔒 ENCRYPTION: ACTIVE ✅
User ID: [yyyyyyyy] (KHÁC với Tab 1) ⭐ QUAN TRỌNG
```

---

### Test 2: Message Sync - USER 1 Gửi Tin

**Tab 1: Gửi tin nhắn**
```
Input field: "Này là message từ User 1"
Bấm: [SEND] button
```

**Kiểm tra Tab 1:**
```
Messages area:
├─ [10:30:00] YOU: Này là message từ User 1
└─ Color: Xanh biển (cyanish), border trái xanh lục
```

**Kiểm tra Tab 2 (Tự động nhận):**
```
Messages area:
├─ [10:30:00] USER_XXXXX: Này là message từ User 1
└─ Color: Xanh lá, border trái xanh lá

Chính xác cần:
├─ Hiển thị tin nhắn giống hệt (message text)
├─ Timestamp giống: [10:30:00]
├─ Sender khác: USER_XXXXX (không phải YOU)
└─ Mất ~500ms để hiển thị (polling interval)
```

---

### Test 3: Message Sync - USER 2 Gửi Tin

**Tab 2: Gửi tin nhắn**
```
Input field: "Xin chào User 1!"
Bấm: [SEND] button
```

**Kiểm tra Tab 2:**
```
Messages area:
├─ [10:31:00] YOU: Xin chào User 1!
└─ Color: Xanh biển, border trái xanh lục
```

**Kiểm tra Tab 1 (Tự động nhận):**
```
Messages area:
├─ [10:31:00] USER_YYYYY: Xin chào User 1!
└─ Hiển thị tương tự như test 2
   BUT sender ID khác (USER_YYYYY, không phải User 1)
```

---

### Test 4: Continuous Chat - Nhiều Tin Liên Tiếp

**Tổng quát:**
```
Tab 1: Tin 1
Tab 2: Tin 2
Tab 1: Tin 3
Tab 2: Tin 4
...
```

**Kiểm tra:**
- [ ] Cả 2 tabs đều thấy toàn bộ tin nhắn
- [ ] Tin nhắn của user khác hiển thị với `USER_XXXXX`
- [ ] Tin nhắn của user mình hiển thị với `YOU`
- [ ] Timestamp là chính xác
- [ ] Không có message bị lặp
- [ ] Thứ tự messages giống nhau trên 2 tabs

---

## 📊 Statistics Checking

**Tab 1 - Right Panel:**
```
ENCRYPTION: AES-256 CBC ✅
KEY EXCHANGE: RSA-2048 OAEP ✅
MESSAGES SENT: N (tăng khi gửi tin)
MESSAGES RECEIVED: M (tăng khi nhận tin)
SESSION DURATION: hh:mm:ss (tăng liên tục)
```

**Kiểm tra:**
- [ ] MESSAGES SENT = số tin gửi từ Tab 1
- [ ] MESSAGES RECEIVED = số tin nhận từ Tab 1 (bao gồm User 2)
- [ ] SESSION DURATION tăng dần (00:00:01 → 00:10:00)

---

## 🔍 Debugging - Console F12

**Mở Dev Tools:** `F12` → Console tab

**Normal Logs:**
```javascript
// Khi kết nối thành công
undefined

// Khi fetch messages
undefined

// Không có error ✅
```

**Error Examples (Không nên xảy ra):**
```javascript
❌ Declaration or statement expected (script.js)
❌ Cannot read property 'userId' of undefined
❌ Fetch error on /api/messages
❌ Socket connection failed
```

**Nếu có error:**
1. Refresh page: `F5`
2. Inspect Network tab (`F12` → Network)
3. Xem request `/api/connect`, `/api/send`, `/api/messages`

---

## 🚨 Common Issues & Fixes

### Issue 1: "OFFLINE" Badge - Kết Nối Thất Bại

**Triệu chứng:**
```
Header: 🔴 OFFLINE
[CONNECT] button không hoạt động
Message: "Connection failed: [WinError 10061]"
```

**Nguyên nhân:**
- Port 12345 chưa listen
- Socket server không chạy
- Firewall chặn

**Fix:**
```bash
# 1. Kill process cũ
taskkill /PID <pid> /F

# 2. Check port 12345
netstat -ano | findstr :12345

# 3. Khởi động lại
python run.py
```

---

### Issue 2: Message Không Sync Giữa Tabs

**Triệu chứng:**
```
Tab 1 gửi tin → Tab 2 không nhận
Hoặc: Messages chỉ hiển thị trên 1 tab
```

**Nguyên nhân:**
- Polling interval quá lâu (> 1 giây)
- Backend không lưu message
- JavaScript có error

**Fix:**
```javascript
// Mở Console (F12)
// Kiểm tra:
console.log(window.chatApp)  // Phải có object
console.log(window.chatApp.userId)  // Phải có ID
console.log(window.chatApp.lastMessageCount)  // Phải là number
```

---

### Issue 3: User ID Giống Nhau Trên 2 Tabs

**Triệu chứng:**
```
Tab 1: Connected as User [aaaaaaaa]
Tab 2: Connected as User [aaaaaaaa]  ❌ Giống Tab 1!
```

**Nguyên nhân:**
- Flask session không khác nhau
- Browser cache

**Fix:**
```bash
# 1. Xóa cookies/cache
F12 → Application → Cookies → Delete all

# 2. Mở 2 tabs mới (không từ reload)
# Tab 1: http://localhost:5000
# Tab 2: http://localhost:5000 (từ new tab)

# 3. Inspect User ID
F12 → Console
window.chatApp.userId  # Phải khác nhau
```

---

### Issue 4: Message Bị Lặp

**Triệu chứng:**
```
Tab 1 gửi: "Hi"
Hiển thị: "Hi" × 2 hoặc × 3 lần
```

**Nguyên nhân:**
- `lastMessageCount` tracking sai
- Polling fetch tất cả messages nhiều lần

**Fix:**
```javascript
// Console check
window.chatApp.lastMessageCount  // Phải tăng sau mỗi display
window.chatApp.messageUpdateInterval  // Phải có interval ID
```

---

## ✅ Checklist - All Tests Passed

- [ ] **Test 1**: Tab 1 kết nối → ONLINE ✅
- [ ] **Test 1**: Tab 2 kết nối → ONLINE + USER ID khác
- [ ] **Test 2**: Tab 1 gửi → Tab 2 nhận (with correct sender)
- [ ] **Test 3**: Tab 2 gửi → Tab 1 nhận (with correct sender)
- [ ] **Test 4**: Nhiều tin liên tiếp → Đúng thứ tự
- [ ] **Stats**: MESSAGES SENT/RECEIVED tính đúng
- [ ] **Stats**: SESSION DURATION tăng liên tục
- [ ] **Encryption**: Badge hiển thị "AES-256 CBC"
- [ ] **Console**: Không có error messages
- [ ] **Performance**: Message sync trong < 1 giây

---

## 📈 Performance Metrics

**Tốc độ Sync:**
- Ideal: < 500ms (polling interval)
- Acceptable: 500-1000ms
- Slow: > 1000ms

**Kiểm tra:**
```javascript
// Console
const start = Date.now();
// Gửi tin từ Tab 1
// Đo khi nhận trên Tab 2
const latency = Date.now() - start;
console.log(`Latency: ${latency}ms`);  // Nên < 600ms
```

---

## 🔐 Security Verification

**Tin nhắn có mã hóa không?**
```
Network Tab (F12):
POST /api/send
Body: {"message": "Hello"}
      (Text thường, không mã hóa client-side)

Nhưng:
- Server mã hóa AES-256
- Socket gửi encrypted bytes
```

**Kiểm tra Encryption Status:**
```
Badge: 🔒 ENCRYPTION: ACTIVE ✅
Text: "Encryption active - Secure communication established"
```

---

## 📝 Test Report Template

```
═══════════════════════════════════════════════════════════
         MULTI-USER CHAT TEST REPORT
═══════════════════════════════════════════════════════════

Date: [YYYY-MM-DD]
Tester: [Tên]
Environment: Windows 10, Python 3.x, Chrome

TEST RESULTS:
═════════════════════════════════════════════════════════

[✅ PASS / ❌ FAIL] Test 1: Tab Connection
Notes: ...

[✅ PASS / ❌ FAIL] Test 2: User1 → User2
Notes: ...

[✅ PASS / ❌ FAIL] Test 3: User2 → User1
Notes: ...

[✅ PASS / ❌ FAIL] Test 4: Message Sync
Notes: ...

OVERALL: [✅ PASS / ❌ FAIL]

Issues Found:
- [#1] ...
- [#2] ...

═════════════════════════════════════════════════════════
```

---

## 🎓 Hiểu Biết Sâu Hơn

### Architecture Diagram
```
Client 1 (Tab 1)          Client 2 (Tab 2)
    │                            │
    │ Session: uuid-1            │ Session: uuid-2
    │                            │
    └──────→ Flask Server ←──────┘
             (port 5000)
                 │
                 ├─→ user_sockets {uuid-1: SocketManager1,
                 │                 uuid-2: SocketManager2}
                 │
                 └─→ messages_history = [
                     {sender: 'USER_uuid-1', message: 'Hi'},
                     {sender: 'USER_uuid-2', message: 'Hello'},
                     ...
                 ]
                 
                 ↓ (Socket Connection)
             Socket Server
             (port 12345)
                 │
                 ├─→ RSA Key Exchange
                 ├─→ AES Key Distribution
                 └─→ Message Relay
```

### Message Flow
```
Tab 1 (User A):          Tab 2 (User B):
    │                         │
    └─→ Input: "Hello" ───────┘
        │
        └─→ /api/send
            │
            ├─→ Add to messages_history
            │   {sender: 'USER_A...', message: 'Hello'}
            │
            └─→ Encrypt with Socket
                │
                ↓
           Socket Server
                │
                └─→ Poll /api/messages (every 500ms)
                    │
                    ├─→ Tab 1 sees: YOU: Hello (blue)
                    │
                    └─→ Tab 2 sees: USER_A...: Hello (green)
```

---

**Chúc bạn test thành công! 🎉**
