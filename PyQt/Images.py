from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
import sys

x = 500
y = 100
width = 1280
height = 720

class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(x, y, width, height)
        self.setWindowTitle("Images")
        self.setWindowIcon(QIcon("Assets\\NERC-LOGO-WHITE-BG-min.png"))


def main():
    app = QApplication(sys.argv)
    window = main_window()

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
    