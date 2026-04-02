import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.ecc import Ui_MainWindow
import requests


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_3feraf.clicked.connect(self.call_api_gen_keys)
        self.ui.pushButton_eegge_2.clicked.connect(self.call_api_sign)
        self.ui.pushButton_eegge_3.clicked.connect(self.call_api_verify)

    # ================== GENERATE KEYS ==================
    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/ecc/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                QMessageBox.information(self, "Info", data["message"])
            else:
                QMessageBox.warning(self, "Error", response.text)
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", str(e))

    # ================== SIGN ==================
    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/ecc/sign"

        message = self.ui.plainTextEdiaaw.toPlainText().strip()
        if not message:
            QMessageBox.warning(self, "Warning", "Message is empty!")
            return

        payload = {
            "message": message
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()

                # ✅ FIX QUAN TRỌNG (QPlainTextEdit)
                self.ui.plainTextEdit_4efgd.setPlainText(data["signature"])

                QMessageBox.information(self, "Info", "Signed Successfully")
            else:
                QMessageBox.warning(self, "Error", response.text)

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", str(e))

    # ================== VERIFY ==================
    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/ecc/verify"

        message = self.ui.plainTextEdiaaw.toPlainText().strip()
        signature = self.ui.plainTextEdit_4efgd.toPlainText().strip()

        if not message or not signature:
            QMessageBox.warning(self, "Warning", "Missing message or signature!")
            return

        payload = {
            "message": message,
            "signature": signature
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()

                if data["is_verified"]:
                    QMessageBox.information(self, "Info", "Verified Successfully")
                else:
                    QMessageBox.warning(self, "Info", "Verified Fail")

            else:
                QMessageBox.warning(self, "Error", response.text)

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())