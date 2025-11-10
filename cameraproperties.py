import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QMessageBox, QPushButton,QLabel
from PyQt5 import uic
import serial.tools.list_ports
# from camera import CameraWindow
import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
# Path to your .ui file
cameraprp = r"F:\qtdesigner\cameraconntroll.ui"
serialInst = serial.Serial()


class Camera_control(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(cameraprp, self)  # Load the .ui file dynamically
        self.line_edit = self.findChild(QLineEdit, 'comport') # Find QLineEdit widget by its objectName
        self.appply = self.findChild(QPushButton, "apply")  # Find QPushButton widget by its objectName
#         self.cam = cv2.VideoCapture(0)
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_frame)
#         self.timer.start(20)  # Update every 20 ms
#         self.video_label = self.findChild(QLabel, 'label_8')
#     def update_frame(self):
#         ret, frame = self.cam.read()
#         if ret:
#             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
#             pixmap = QPixmap.fromImage(image)
#             self.video_label.setPixmap(pixmap)
#             self.video_label.setScaledContents(True)
            
        if self.appply:
            self.appply.clicked.connect(self.print_text)
        
        self.left = self.findChild(QPushButton, "left_2")  # Find the left button
        self.right = self.findChild(QPushButton, "right")  # Find the left button
        if self.left:
            self.left.pressed.connect(self.left_press)
            self.left.released.connect(self.left_released)
        
        if self.right:
            self.right.pressed.connect(self.right_press)
            self.right.released.connect(self.right_released)
    def print_text(self): 
        text = self.line_edit.text()
        if text: 
            self.comportt(text)
        else:
            self.show_error_message("Error: No Port Number found!")
    
    def comportt(self, text):
        use = "COM" + text
        print(use)
        serialInst.baudrate = 115200
        serialInst.port = use
        try:
            serialInst.open()
        except serial.SerialException as e:
            self.show_error_message(f"Could not open port {use}:\n{str(e)}")
        
    def left_press(self):
        command = str('O')  # Send 'left' with newline character
        serialInst.write(command.encode('utf-8'))
        print("left pressed")
            
    def left_released(self):
        command = 'F'  # Send 'off' with newline character
        serialInst.write(command.encode('utf-8'))

    def right_press(self):
        command = str('r')  # Send 'left' with newline character
        serialInst.write(command.encode('utf-8'))
        print("right pressed")
            
    def right_released(self):
        command = 'm'  # Send 'off' with newline character
        serialInst.write(command.encode('utf-8'))

    def show_error_message(self, message): 
        error_msg = QMessageBox() 
        error_msg.setIcon(QMessageBox.Critical) 
        error_msg.setWindowTitle("Error") 
        error_msg.setText(message) 
        error_msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Camera_control()
    main_window.show()
    sys.exit(app.exec_())
