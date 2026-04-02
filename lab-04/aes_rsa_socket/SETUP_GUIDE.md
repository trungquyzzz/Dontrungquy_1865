# 🔧 SETUP GUIDE - Secure Chat

Hướng dẫn chi tiết cài đặt và cấu hình Secure Chat trên các hệ điều hành.

---

## 💻 Windows 10/11

### Step 1: Cài đặt Python

1. Tải Python từ: https://www.python.org/downloads/
2. Chọn version 3.9+ (có checkmark "Add Python to PATH")
3. Chạy installer
4. Verify:
   ```bash
   python --version
   ```

### Step 2: Clone/Download Project

1. Giải nén thư mục `aes_rsa_socket`
2. Mở Command Prompt (Win + R → cmd)
3. Chuyển đến thư mục:
   ```bash
   cd "đường dẫn\aes_rsa_socket"
   ```

### Step 3: Tạo Virtual Environment (Optional nhưng recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

### Step 4: Cài đặt Dependencies

```bash
pip install -r requirements.txt
```

Sẽ cài đặt:
- Flask 2.3.2
- PyCryptodome
- Python-socketio
- Flask-cors

### Step 5: Chạy Ứng Dụng

**Cách 1 - Dùng Batch File (Dễ nhất):**
```bash
run.bat
```
Hoặc double-click `run.bat`

**Cách 2 - Dùng Python Script:**
```bash
python run.py
```

**Cách 3 - Chạy Services riêng:**
```bash
# Terminal 1: Socket Server
python server.py

# Terminal 2: Flask Web Server
python web_server.py
```

### Step 6: Truy cập Giao diện

Mở browser → Nhập: `http://localhost:5000`

---

## 🐧 Linux (Ubuntu/Debian)

### Step 1: Cài đặt Python

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 --version
```

### Step 2: Chuẩn bị Project

```bash
cd /đường/dẫn/đến/aes_rsa_socket
```

### Step 3: Tạo Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Cài đặt Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Chạy Ứng dụng

```bash
python run.py
```

Hoặc chạy riêng:
```bash
# Terminal 1
python server.py

# Terminal 2 (new window)
python web_server.py
```

### Step 6: Truy cập

Browser → `http://localhost:5000`

---

## 🍎 macOS

### Step 1: Cài đặt Python

**Dùng Homebrew (recommended):**
```bash
brew install python@3.11
python3 --version
```

**Hoặc tải từ:** https://www.python.org/

### Step 2: Setup Project

```bash
cd /path/to/aes_rsa_socket
```

### Step 3: Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Cài Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Chạy

```bash
python run.py
```

### Step 6: Truy cập

Browser → `http://localhost:5000`

---

## 🌐 Chạy trên Network

### Scenario: Server trên Máy A, Client trên Máy B

#### Máy A (Server):

1. Kiểm tra IP:
   - Windows: `ipconfig` → IPv4 Address
   - Linux/Mac: `ifconfig` hoặc `hostname -I`

2. Cấu hình `web_server.py`:
   ```python
   app.run(debug=True, host='0.0.0.0', port=5000)
   # 0.0.0.0 = listen trên tất cả interfaces
   ```

3. Chạy:
   ```bash
   python run.py
   ```
   Ghi nhớ IP: VD `192.168.1.100`

#### Máy B (Client):

1. Mở browser
2. Nhập: `http://192.168.1.100:5000`
3. Settings:
   - Host: `192.168.1.100`
   - Port: `12345`
4. Connect!

---

## 🔒 Firewall Configuration

Nếu không kết nối được, cần cho phép Firewall:

### Windows Firewall:
1. Settings → Privacy & Security → Windows Defender Firewall
2. Advanced settings
3. Inbound Rules → New Rule
4. Port 12345 (TCP) → Allow

### Linux Firewall:
```bash
sudo ufw allow 12345/tcp
sudo ufw allow 5000/tcp
sudo ufw enable
```

### macOS:
```bash
# Thường không cần, hoặc:
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate on
```

---

## 🧪 Testing

### Test 1: Kiểm tra Socket Server
```bash
# Terminal 1
python server.py
# Output: Chờ connection...

# Terminal 2
python client.py
# Output: Kết nối + mã hóa hoạt động
```

### Test 2: Kiểm tra Web Server
```bash
python web_server.py
# Output: Running on http://127.0.0.1:5000
```

### Test 3: Kiểm tra End-to-End
1. Chạy `python run.py`
2. Mở Browser → `http://localhost:5000`
3. Connect → Send message
4. Kiểm tra Socket Server logs

---

## ⚙️ Configuration

### Port Mặc định:
- Socket Server: `12345`
- Web Server: `5000`

### Thay đổi Port:

**Socket Server (server.py):**
```python
server_socket.bind(('localhost', 9999))  # Thay 12345 → 9999
```

**Web Server (web_server.py):**
```python
app.run(debug=True, host='0.0.0.0', port=8888)  # Thay 5000 → 8888
```

**Client Web (static/script.js):**
```javascript
const response = await fetch('/api/connect', {
    // ... đã config trong web_server.py
});
```

---

## 🐛 Debugging

### Xem Logs:

Mở Browser DevTools: `F12` → Console

### Common Errors:

| Error | Nguyên nhân | Giải pháp |
|-------|-----------|----------|
| Connection refused | Server không chạy | `python server.py` |
| Port already in use | Port bị chiếm | Đổi port hoặc kill process |
| Module not found | Thiếu dependency | `pip install -r requirements.txt` |
| CORS Error | Cross-origin issue | Kiểm tra Flask-CORS config |

### Xem Chi tiết:

**Terminal:**
- Kiểm tra console output của server.py và web_server.py

**Browser (DevTools):**
- Console (F12) → Xem error messages
- Network tab → Xem requests/responses
- Application → Xem localStorage/cookies

---

## 🔐 Production Setup

⚠️ **Cảnh báo**: Cấu hình dưới đây là cho Production, không dùng trong Dev.

### 1. Tắt Debug Mode:
```python
app.run(debug=False, host='0.0.0.0', port=5000)
```

### 2. Dùng Production Server (Gunicorn):
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 web_server:app
```

### 3. Dùng HTTPS:
```bash
pip install pyopenssl
# Tạo certificate...
```

### 4. Load Balancing:
Dùng Nginx hoặc Apache để proxy requests

### 5. Database:
Lưu trữ messages vào DB thay vì memory

---

## 📊 System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| Python | 3.7 | 3.9+ |
| RAM | 256 MB | 512 MB+ |
| Disk | 50 MB | 100 MB+ |
| Network | 10 Mbps | 100 Mbps+ |
| Browser | Any modern | Chrome, Firefox, Edge |

---

## ✅ Checklist Setup

- [ ] Python 3.7+ installed
- [ ] Virtual environment created (optional)
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Port 12345 available (socket server)
- [ ] Port 5000 available (web server)
- [ ] Firewall allows ports
- [ ] `run.py` or `run.bat` executable
- [ ] Browser modern (Chrome, Firefox, etc.)
- [ ] Test connection successful

---

## 🚀 Tối ưu Hóa

### Tốc độ:
1. Dùng SSD (nhanh hơn HDD)
2. Close ứng dụng không cần thiết
3. Dùng wired connection (không WiFi)

### Bảo mật:
1. Tắt debug mode
2. Dùng strong passwords
3. Enable HTTPS
4. Keep library updated: `pip install --upgrade -r requirements.txt`

### Scalability:
1. Dùng async/await
2. Implement connection pooling
3. Add database layer
4. Deploy với multiple workers

---

## 📚 Tham Khảo

- Python: https://www.python.org/
- Flask: https://flask.palletsprojects.com/
- PyCryptodome: https://pycryptodome.readthedocs.io/
- AES: https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf
- RSA: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-56ar3.pdf

---

**Xong! Bạn đã sẵn sàng sử dụng Secure Chat! 🎉🔐**
