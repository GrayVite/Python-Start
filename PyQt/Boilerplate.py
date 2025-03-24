# First intro to PyQt5


# Boilerplate code for a basic window
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class main_window(QMainWindow):
    def __init__(self):
        super().__init__()


def main():
    app = QApplication(sys.argv)
    window = main_window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()