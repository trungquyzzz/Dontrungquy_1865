import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Kết nối các nút bấm theo tên widget trong file .ui của bạn
        self.ui.pushButton_3feraf.clicked.connect(self.call_api_gen_keys)
        self.ui.pushButtongsr.clicked.connect(self.call_api_encrypt)
        self.ui.pushButton_eegge.clicked.connect(self.call_api_decrypt)
        self.ui.pushButton_eegge_2.clicked.connect(self.call_api_sign)
        self.ui.pushButton_eegge_3.clicked.connect(self.call_api_verify)

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(response.json().get("message", "Success"))
                msg.exec_()
        except Exception as e:
            print(f"Error: {e}")

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        payload = {
            "message": self.ui.plainTextEdit_3ttn.toPlainText(),
            "key_type": "public"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # Hiển thị kết quả mã hóa Hex vào ô CipherText
                self.ui.plainTextEdit_2yrye.setPlainText(data["encrypted_message"])
                QMessageBox.information(self, "Thông báo", "Mã hóa thành công!")
        except Exception as e:
            print(f"Error: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        payload = {
            "ciphertext": self.ui.plainTextEdit_2yrye.toPlainText(),
            "key_type": "private"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # Trả kết quả giải mã về ô PlainText ban đầu
                self.ui.plainTextEdit_3ttn.setPlainText(data["decrypted_message"])
                QMessageBox.information(self, "Thông báo", "Giải mã thành công!")
        except Exception as e:
            print(f"Error: {e}")

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"
        payload = {"message": self.ui.plainTextEdiaaw.toPlainText()}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                self.ui.plainTextEdit_4efgd.setPlainText(response.json()["signature"])
                QMessageBox.information(self, "Thông báo", "Ký số thành công!")
        except Exception as e:
            print(f"Error: {e}")

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"
        payload = {
            "message": self.ui.plainTextEdiaaw.toPlainText(),
            "signature": self.ui.plainTextEdit_4efgd.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                is_valid = response.json().get("is_verified")
                status = "Hợp lệ!" if is_valid else "Không hợp lệ hoặc đã bị chỉnh sửa!"
                QMessageBox.information(self, "Kết quả xác thực", status)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())