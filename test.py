import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction, QFileDialog, QLabel, QDialog, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from camerraprop import Camera_Option
from cameraproperties import Camera_control

# Path to your .ui files
ui_file_path = r"F:\qtdesigner\maino.ui"
# uii = r"F:\qtdesigner\workspace.ui"
# uiii = r"F:\qtdesigner\circuit.ui"
ui_file= r"F:\qtdesigner\new menu.ui"
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file_path, self)  # Load the .ui file dynamically

        # Assuming the button in your .ui file has the objectName 'New'
        self.new_button = self.findChild(QPushButton, 'New')
        if self.new_button:  # Ensure the button is found
            self.new_button.clicked.connect(self.open_new_window)

        # Assuming the menu action in your .ui file has the objectName 'actionnew'
        self.newone_action = self.findChild(QAction, 'actionnew')
        if self.newone_action:  # Ensure the action is found
            self.newone_action.triggered.connect(self.open_new_window)

    def open_new_window(self):
        self.new_window = NewWindow()  # Pass the parameter to the new window
        self.new_window.show()
        # self.close()

class NewWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)  # Load the .ui file dynamically

                # Let's assume your buttons are named pushButton1, pushButton2, ..., pushButton5 in the .ui file
        self.selected_button = None  # Keep track of which button was clicked

        # Connect your custom buttons to a common method
        self.pushButton.clicked.connect(lambda: self.set_button("Button 1"))
        self.pushButton_2.clicked.connect(lambda: self.set_button("Button 2"))
        self.pushButton_3.clicked.connect(lambda: self.set_button("Button 3"))
        self.pushButton_4.clicked.connect(lambda: self.set_button("Button 4"))
        self.pushButton_5.clicked.connect(lambda: self.set_button("Button 5"))
        self.pushButton_6.clicked.connect(lambda: self.set_button("Button 6"))
        self.pushButton_7.clicked.connect(lambda: self.set_button("Button 7"))

        # Connect the OK button in the button box
        self.buttonBox.accepted.connect(self.ok_clicked)

    def set_button(self, name):
        self.selected_button = name
        # print(f"{name} clicked")

    def ok_clicked(self):
        if self.selected_button == "Button 2":
            print(f"OK clicked after selecting Button 2")
            self.open_new_window()
        else:
            print("OK clicked without selecting a button")


    def open_new_window(self):
        self.new_window = Camera_control() # Pass the parameter to the new window
        self.new_window.show()
    

        # self.push = self.findChild(QPushButton, "addlayout")
        # self.push.clicked.connect(self.clicked)

    # def clicked(self):
    #     self.new_window = NewWindowWithPixmap()
    #     self.new_window.show()
    #     self.close()
 
# class NewWindowWithPixmap(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi(uiii, self)  # Load the .ui file dynamically
#         fname= QFileDialog.getOpenFileName(self, "open file", "", "ALL FILES (*);;PDF File (*.pdf)")        
#         if fname:
#             # self.label = self.findChild(QLabel, 'label')  # Ensure QLabel is correctly defined in your .ui file
#             self.pixmap = QPixmap(fname[0])
#             self.label.setPixmap(self.pixmap)
#         self.push = self.findChild(QPushButton, "pushButton_3")
#         self.push.clicked.connect(self.clicked)
#         self.cameraproperties=self.findChild(QPushButton,"pushButton_5")
#         self.cameraproperties.clicked.connect(self.camerapropertie)
    
#     def clicked(self):
#         fname= QFileDialog.getOpenFileName(self, "open file", "", "ALL FILES (*);;PDF File (*.pdf)")        
#         if fname:
#             # self.label = self.findChild(QLabel, 'label')  # Ensure QLabel is correctly defined in your .ui file
#             self.pixmap = QPixmap(fname[0])
#             self.label.setPixmap(self.pixmap)
    
#     def camerapropertie(self):
#         self.new_window = Camera_Option()
#         self.new_window.show()
             
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
