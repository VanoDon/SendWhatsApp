import sys
import webbrowser
import time
from urllib.parse import quote
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QTextEdit, QPushButton, QLabel

class WhatsAppSender(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('WhatsApp Message Sender')

        layout = QVBoxLayout()

        self.numberLabel = QLabel('Number (Starting with 27, no spaces):')
        layout.addWidget(self.numberLabel)

        self.numberInput = QLineEdit()
        layout.addWidget(self.numberInput)

        self.messageLabel = QLabel('Enter your message:')
        layout.addWidget(self.messageLabel)

        self.messageInput = QTextEdit()
        layout.addWidget(self.messageInput)

        self.sendButton = QPushButton('Send Message')
        self.sendButton.clicked.connect(self.send_message)
        layout.addWidget(self.sendButton)

        self.setLayout(layout)

    def send_message(self):
        num = self.numberInput.text().replace(" ", "").replace("+", "")
        text = self.messageInput.toPlainText()
        encoded_text = quote(text)

        url = f"whatsapp://send?phone={num}"
        webbrowser.open(url)

        time.sleep(1)
        webbrowser.open(url)
        time.sleep(1)

        url = f"whatsapp://send?phone={num}&text={encoded_text}"
        webbrowser.open(url)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WhatsAppSender()
    ex.show()
    sys.exit(app.exec_())
