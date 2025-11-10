import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction
from PyQt5 import uic

# Path to your .ui files
ui_file_path = r"F:\qtdesigner\testone.ui"
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file_path, self)  # Load the .ui file dynamically
        self.push=self.findChild(QPushButton,"pushButton")
        self.push.clicked.connect(self.clicked)
    def clicked(self):
        self.label.setText("hii")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
