import sys
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt # for alignments

x = 500
y = 100
width = 720
height = 1280

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Another Window")
        self.setGeometry(x, y, height, width)
        self.setWindowIcon(QIcon("Assets\\NERC-LOGO-WHITE-BG-min.png"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 36))
        label.setGeometry(0, 0, 1280, 100)
        label.setStyleSheet("color: #292929;"
                            "background-color: #6fdcf7;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;") # Used to add CSS
        
        #label.setAlignment(Qt.AlignTop) # Vertically Top, for bottom use AlignBottom, for center use AlignVCenter
        #label.setAlignment(Qt.AlignRight) # Horizontally align right, for left AlignLeft
        #label.setAlignment(Qt.AlignHCenter)

        # Combining effects of both using OR operator
        # For same effect AlignCenter
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()