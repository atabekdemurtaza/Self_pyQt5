import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Простой интерфейс')

        self.label = QLabel('Привет, мир!', self)
        self.label.move(100, 50)

        self.button = QPushButton('Нажми меня', self)
        self.button.move(100, 100)
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        self.label.setText('Кнопка нажата!')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec_())
