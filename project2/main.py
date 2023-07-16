import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QTextEdit, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Расширенный интерфейс')

        self.label = QLabel('Привет, мир!', self)
        self.label.move(150, 20)

        self.name_label = QLabel('Имя:', self)
        self.name_label.move(30, 60)

        self.name_input = QLineEdit(self)
        self.name_input.move(100, 60)

        self.message_label = QLabel('Сообщение:', self)
        self.message_label.move(30, 100)

        self.message_input = QTextEdit(self)
        self.message_input.move(100, 100)
        self.message_input.resize(200, 100)

        self.button = QPushButton('Отправить', self)
        self.button.move(150, 220)
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        name = self.name_input.text()
        message = self.message_input.toPlainText()

        if name and message:
            self.label.setText(f'Привет, {name}! Сообщение получено.')
            self.name_input.clear()
            self.message_input.clear()
        else:
            self.label.setText('Введите имя и сообщение.')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec_())
