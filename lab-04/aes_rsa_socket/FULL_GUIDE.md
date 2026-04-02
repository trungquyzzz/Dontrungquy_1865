# 📖 HƯỚNG DẪN ĐỦ ĐẦY - AES-RSA Socket Chat Multi-User

## 🎯 TÓM TẮT DỰ ÁN

Đây là **ứng dụng chat bảo mật** cho phép:
- ✅ **2+ users** trò chuyện trên **1 server**
- ✅ **AES-256** mã hóa tất cả tin nhắn
- ✅ **RSA-2048** trao đổi khóa an toàn
- ✅ **Real-time sync** tin nhắn giữa users (~500ms)
- ✅ **Hacker UI** với dark theme & neon colors
- ✅ **Session tracking** & security dashboard

---

## 📋 ĐỌC HƯỚNG DẪN (THEO THỨ TỰ)

### 📌 BƯỚC 1: Quick Reference (2 min)
**File:** `QUICK_REFERENCE.md`  
**Nội dung:** Commands cheatsheet, API, shortcuts  
**Dành cho:** Người muốn quick commands

### 📌 BƯỚC 2: Usage Guide (5 min) ⭐ **CHÍNH ĐỒNG**
**File:** `USAGE_GUIDE.md`  
**Nội dung:** Step-by-step từ cài đặt đến test multi-user  
**Dành cho:** Người lần đầu chạy project

### 📌 BƯỚC 3: Testing Multi-User (Khi cần debug)
**File:** `TESTING_MULTIUSER.md`  
**Nội dung:** Chi tiết test procedures, checklist, troubleshooting  
**Dành cho:** Testing & debugging

### 📌 BƯỚC 4: Summary (5 min)
**File:** `SUMMARY.md`  
**Nội dung:** Tổng quan project, tính năng, tech stack  
**Dành cho:** Hiểu overview

### 📌 BƯỚC 5: README (15 min)
**File:** `README.md`  
**Nội dung:** Tài liệu đầy đủ chi tiết  
**Dành cho:** Deep dive

### 📌 BƯỚC 6: Setup Guide (Nếu lỗi)
**File:** `SETUP_GUIDE.md`  
**Nội dung:** Cài đặt chi tiết, firewall, production  
**Dành cho:** Troubleshooting & deployment

### 📌 BƯỚC 7: Design (Nếu customize UI)
**File:** `DESIGN.md`  
**Nội dung:** Giao diện, color, components  
**Dành cho:** Customize UI/UX

### 📌 BƯỚC 8: Index (Tham khảo code)
**File:** `INDEX.md`  
**Nội dung:** Code reference, file structure  
**Dành cho:** Code exploration

---

## ⚡ QUICK START (3 BƯỚC)

```bash
# 1️⃣ Cài dependencies
pip install -r requirements.txt

# 2️⃣ Chạy server
python run.py

# 3️⃣ Mở browser
# Tab 1: http://localhost:5000 → CONNECT
# Tab 2: http://localhost:5000 → CONNECT
# Test gửi/nhận tin ✅
```

---

## 🔍 ĐỌC CÁI GÌ TRƯỚC?

### 🔴 Bạn chỉ muốn **chạy ngay**?
```
→ Đọc: USAGE_GUIDE.md (5 min)
→ Chạy: python run.py
→ Test: 2 tabs, gửi/nhận tin
→ Xong! ✅
```

### 🟠 Bạn muốn **hiểu hoạt động**?
```
→ Đọc: SUMMARY.md (5 min)
→ Đọc: USAGE_GUIDE.md (5 min)
→ Đọc: README.md (15 min)
→ Chạy: python run.py
→ Test thoải mái ✅
```

### 🟡 Bạn muốn **customize/deploy**?
```
→ Đọc: USAGE_GUIDE.md (5 min)
→ Đọc: SETUP_GUIDE.md (10 min)
→ Vào code: web_server.py, style.css, etc.
→ Sửa & test ✅
```

### 🟢 Bạn gặp **lỗi/vấn đề**?
```
→ Đọc: QUICK_REFERENCE.md (troubleshooting)
→ Đọc: TESTING_MULTIUSER.md (debug)
→ Mở F12 Console check errors
→ Fix & retry ✅
```

---

## 📁 DANH SÁCH FILES ĐÃ CẬP NHẬT

### 📚 Documentation Files (NEW/Updated)
```
✅ START_HERE.md              ← Updated (Index tất cả docs)
✅ USAGE_GUIDE.md            ← NEW (Step-by-step guide)
✅ QUICK_REFERENCE.md        ← NEW (Commands cheatsheet)
✅ TESTING_MULTIUSER.md      ← NEW (Test procedures)
✅ SUMMARY.md                ← Updated (Added multi-user features)
📖 README.md                 ← Main documentation
📖 QUICK_START.md            ← Quick launch
📖 SETUP_GUIDE.md            ← Installation guide
📖 DESIGN.md                 ← UI/UX design
📖 INDEX.md                  ← Code reference
```

### 💻 Code Files (FIXED)
```
✅ web_server.py             ← Fixed message sync (shared history)
✅ script.js                 ← Fixed message display logic
✅ server.py                 ← Socket server (no changes needed)
✅ run.py                    ← Main entry point
```

### 🎨 Frontend Files
```
📦 templates/chat.html       ← HTML interface
📦 static/style.css          ← CSS (hacker theme)
📦 static/script.js          ← JavaScript (FIXED)
```

---

## 🚀 RUN PROJECT - EXACT STEPS

### Step 1: Prepare
```bash
cd c:\Users\Mr Quy\Downloads\Dontrungquy_1865\Dontrungquy_1865\lab-04\aes_rsa_socket

pip install -r requirements.txt
```

### Step 2: Run
```bash
python run.py
```

Output sẽ hiển thị:
```
 * Running on http://127.0.0.1:5000
 * Socket Server listening on localhost:12345
```

### Step 3: Browser
```
Tab 1: http://localhost:5000
       Click [CONNECT] button
       Status: 🟢 ONLINE ✅
       
Tab 2: http://localhost:5000 (new tab)
       Click [CONNECT] button
       Status: 🟢 ONLINE ✅
       USER ID: (khác Tab 1) ✅
```

### Step 4: Test
```
Tab 1: Type "Xin chào" → [SEND]
       → Hiển thị: YOU: Xin chào ✅

Tab 2: Auto-receive
       → Hiển thị: USER_XXXXX: Xin chào ✅
       → Takes ~500ms (normal)

Tab 2: Type "Xin chào anh!" → [SEND]
       → Hiển thị: YOU: Xin chào anh! ✅

Tab 1: Auto-receive
       → Hiển thị: USER_YYYYY: Xin chào anh! ✅
```

### ✅ Success Criteria
- [ ] Cả 2 tabs ONLINE
- [ ] User ID khác nhau
- [ ] Messages sync giữa tabs
- [ ] Sender ID đúng (USER_XXX hoặc YOU)
- [ ] Timestamps chính xác
- [ ] Encryption badge ACTIVE
- [ ] No console errors (F12)

---

## 🔧 CONFIGURATION

### Default Ports
```
Web Server:   localhost:5000
Socket Server: localhost:12345
```

### Change Ports
```python
# In run.py:
app.run(debug=True, host='0.0.0.0', port=8000)  # Web port

# In server.py + web_server.py:
server_socket.bind(('localhost', 12346))  # Socket port
```

### Remote Access
```python
# In run.py, change to:
app.run(debug=True, host='0.0.0.0', port=5000)

# Then access from: http://<Server-IP>:5000
```

---

## 🐛 COMMON ISSUES & FIXES

### ❌ "Address already in use" - Port 5000/12345
```bash
# Find & kill process
netstat -ano | findstr :5000
taskkill /PID <pid> /F

# Restart
python run.py
```

### ❌ "OFFLINE" Badge - Can't Connect
```bash
# Check socket server running
netstat -ano | findstr :12345

# Firewall issue?
# OR port 12345 in use
# → Kill & restart
```

### ❌ Messages Not Syncing - JavaScript Error
```bash
# Open F12 Developer Tools
# Console tab → check errors
# If error: Refresh F5
# Still error: Restart server
```

### ❌ Same User ID on 2 Tabs
```bash
# Clear cookies
F12 → Application → Cookies → Delete all

# Open fresh tabs (not reload)
Ctrl+T → http://localhost:5000
Ctrl+T → http://localhost:5000
```

### ❌ "ModuleNotFoundError"
```bash
# Reinstall packages
pip install -r requirements.txt --upgrade
```

---

## 📊 Architecture Overview

```
┌─────────────┐              ┌─────────────┐
│ Browser T1  │              │ Browser T2  │
│  (User A)   │              │  (User B)   │
└──────┬──────┘              └──────┬──────┘
       │                            │
       └────────→ Flask Server ←────┘
                  (port 5000)
                       ↓
                 ┌────────────────┐
                 │ user_sockets   │
                 │ {id-A: socket-A│
                 │  id-B: socket-B│
                 └────────────────┘
                       ↓
                 ┌────────────────┐
                 │ messages_history
                 │ [{from-A, text}
                 │  {from-B, text}
                 │  ...]          │
                 └────────────────┘
                       ↓
               Socket Server (12345)
         (RSA Exchange + Message Relay)
```

---

## 🔐 SECURITY FLOW

```
1. Connection
   └─ User → /api/connect → Session UUID created
   └─ Generate RSA-2048 keys
   └─ Exchange public keys
   └─ Receive AES-256 key (encrypted)

2. Message Send
   └─ User types message
   └─ Encrypt with AES-256 (random IV)
   └─ Send to /api/send
   └─ Save to shared history
   └─ Broadcast via Socket

3. Message Receive
   └─ Poll /api/messages every 500ms
   └─ Get full message history
   └─ Filter: Own = "YOU", Others = "USER_XXX"
   └─ Display on UI
```

---

## 🎯 NEXT STEPS

### To Learn More
1. Read `README.md` (complete documentation)
2. Explore `web_server.py` (Flask backend logic)
3. Check `script.js` (client-side JavaScript)
4. Read `DESIGN.md` (UI customization)

### To Customize
1. Change colors: `style.css`
2. Modify layout: `chat.html` + `style.css`
3. Add features: `script.js` + `web_server.py`

### To Deploy
1. Follow `SETUP_GUIDE.md`
2. Use HTTPS (not HTTP)
3. Move to 0.0.0.0 listener
4. Use production WSGI server

### To Debug
1. Open F12 (Developer Tools)
2. Check Console for errors
3. Check Network tab for API calls
4. Read `TESTING_MULTIUSER.md`

---

## ✅ CHECKLIST - YOU'RE READY!

- [ ] Download project ✅
- [ ] Install Python 3.7+ ✅
- [ ] Run `pip install -r requirements.txt` ✅
- [ ] Run `python run.py` ✅
- [ ] Open 2 browser tabs ✅
- [ ] Connect both tabs ✅
- [ ] Send message Tab 1 ✅
- [ ] Receive on Tab 2 ✅
- [ ] Send message Tab 2 ✅
- [ ] Receive on Tab 1 ✅
- [ ] Check ENCRYPTION: ACTIVE ✅
- [ ] All tests passed ✅

**🎉 CONGRATULATIONS! Your multi-user secure chat is working!**

---

## 📞 SUPPORT & RESOURCES

### Stuck? Start Here:
1. **Quick commands?** → `QUICK_REFERENCE.md`
2. **Step-by-step?** → `USAGE_GUIDE.md`
3. **Multi-user test?** → `TESTING_MULTIUSER.md`
4. **Full docs?** → `README.md`
5. **Setup issues?** → `SETUP_GUIDE.md`

### File Structure:
- **📚 Docs:** START_HERE.md, USAGE_GUIDE.md, etc.
- **💻 Code:** web_server.py, server.py, run.py
- **🎨 UI:** templates/chat.html, static/style.css, static/script.js

### Key Technologies:
- **Web:** Flask (Python)
- **Socket:** Python socket module
- **Crypto:** PyCryptodome (AES-256, RSA-2048)
- **Frontend:** HTML5 + CSS3 + JavaScript

---

## 🎓 PROJECT STATS

```
├─ Total Assets: 9+ documentation files
├─ Code Files: 4 (web_server.py, server.py, chat.html, script.js)
├─ Magic Lines: ~1000+ lines of code
├─ Features: 15+ (encryption, sync, UI, security, etc.)
├─ Multi-user: ✅ Fully supported
├─ Real-time: ✅ ~500ms latency
├─ Security: ✅ AES-256 + RSA-2048
└─ Status: 🟢 Ready to use!
```

---

**Good luck! Enjoy your secure chat! 🔐💬**
