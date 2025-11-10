# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
# from PyQt5.QtCore import QTimer
# from PyQt5.QtGui import QImage, QPixmap
# from PyQt5 import uic
# import cv2

# # Path to your .ui file
# ui_file_path = r'F:\qtdesigner\cameraOptions.ui'

# class CameraWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
        
#         # Load the UI file
#         uic.loadUi(ui_file_path, self)
        
#         # Find the QWidget by its objectName
#         self.video_widget = self.findChild(QWidget, 'widget')
#         if not self.video_widget:
#             print("Error: 'widget' not found.")
#             sys.exit()
        
#         # Find the QLabel inside the QWidget
#         self.video_label = self.findChild(QLabel, 'label_8')
#         if not self.video_label:
#             print("Error: 'label' not found.")
#             sys.exit()
        
#         self.cam = cv2.VideoCapture(0)
#         if not self.cam.isOpened():
#             print("Failed to open camera.")
#             sys.exit()
        
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_frame)
#         self.timer.start(20)  # Update every 20 ms

#     def update_frame(self):
#         ret, frame = self.cam.read()
#         if ret:
#             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
#             pixmap = QPixmap.fromImage(image)
#             self.video_label.setPixmap(pixmap)
#             self.video_label.setScaledContents(True)

#     def closeEvent(self, event):
#         self.cam.release()
#         cv2.destroyAllWindows()
#         event.accept()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = CameraWindow()
#     window.show()
#     sys.exit(app.exec_())

# import ctypes
# import _ctypes
# import sys
# import numpy as np
# import cv2

# from pykinect2 import PyKinectRuntime
# from pykinect2.PyKinectV2 import *

# # Initialize Kinect runtime object for color stream
# kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color)

# def main():
#     while True:
#         if kinect.has_new_color_frame():
#             frame = kinect.get_last_color_frame()
#             frame = frame.reshape((1080, 1920, 4)).astype(np.uint8)
#             frame = cv2.resize(frame, (960, 540))  # Resize for display
#             frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)  # Drop alpha channel

#             cv2.imshow('Kinect RGB Camera', frame)

#         # Press 'q' to quit
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     kinect.close()
#     cv2.destroyAllWindows()

# if __name__ == '__main__':
#     main()
# import cv2

# # Try different indices (0, 1, 2, etc.) if the first doesn't work
# cap = cv2.VideoCapture(2)

# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()

# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()
    
#     # If frame is read correctly, ret is True
#     if not ret:
#         print("Can't receive frame. Exiting...")
#         break
    
#     # Display the resulting frame
#     cv2.imshow('Camera Feed', frame)
    
#     # Press 'q' to exit
#     if cv2.waitKey(1) == ord('q'):
#         break

# # Release everything when done
# cap.release()
# cv2.destroyAllWindows()

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

# class SimpleApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Simple PyQt5 App")
#         self.setGeometry(100, 100, 300, 200)  # x, y, width, height
        
#         # Create central widget and layout
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
#         layout = QVBoxLayout()
        
#         # Create a label
#         self.label = QLabel("Hello, PyQt5!")
#         layout.addWidget(self.label)
        
#         # Create a button
#         self.button = QPushButton("Click Me")
#         self.button.clicked.connect(self.on_button_click)
#         layout.addWidget(self.button)
        
#         # Set the layout
#         central_widget.setLayout(layout)
    
#     def on_button_click(self):
#         self.label.setText("Button was clicked!")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = SimpleApp()
#     window.show()
#     sys.exit(app.exec_())

import sys
import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class CameraApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Simple Camera App")
        self.setGeometry(100, 100, 800, 600)
        
        # Create a label to display the camera feed
        self.image_label = QLabel(self)
        self.image_label.setScaledContents(True)
        
        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        self.setLayout(layout)
        
        # Initialize the camera
        self.cap = cv2.VideoCapture(2)
        if not self.cap.isOpened():
            print("Cannot open camera")
            sys.exit(1)
            
        # Set up a timer to update the camera feed
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # Update every 30ms (~33fps)
        
    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # Convert the frame from BGR to RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Convert to QImage
            h, w, ch = frame_rgb.shape
            bytes_per_line = ch * w
            qt_image = QImage(frame_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
            
            # Display the image
            self.image_label.setPixmap(QPixmap.fromImage(qt_image))
            
    def closeEvent(self, event):
        # Release the camera when the app closes
        self.cap.release()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CameraApp()
    window.show()
    sys.exit(app.exec_())