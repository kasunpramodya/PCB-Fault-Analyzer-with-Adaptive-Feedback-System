# import cv2

# def scan_cameras(max_devices=10):
#     available_cameras = []
#     for i in range(max_devices):
#         cap = cv2.VideoCapture(i)
#         if cap.isOpened():
#             print(f"✅ Camera found at index {i}")
#             available_cameras.append(i)
#             cap.release()
#         else:
#             print(f"❌ No camera at index {i}")
#     return available_cameras

# if __name__ == "__main__":
#     cameras = scan_cameras()
#     print("\nAvailable camera indices:", cameras)
# import cv2
# import win32com.client

# def list_cameras(max_devices=10):
#     available_cams = []
#     for i in range(max_devices):
#         cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)  # Use DirectShow on Windows
#         if cap.isOpened():
#             available_cams.append(i)
#             cap.release()
#     return available_cams

# def get_camera_names():
#     system_devices = win32com.client.Dispatch("WbemScripting.SWbemLocator")
#     wbem_services = system_devices.ConnectServer(".", "root\\CIMV2")
#     devices = wbem_services.ExecQuery("SELECT * FROM Win32_PnPEntity WHERE Description LIKE '%camera%' OR Description LIKE '%Video%'")
#     camera_names = [device.Description for device in devices]
#     return camera_names

# if __name__ == "__main__":
#     indices = list_cameras()
#     names = get_camera_names()

#     print("🧠 Available Camera Indices (usable by OpenCV):", indices)
#     print("📷 Detected Camera Names from Windows:")
#     for name in names:
#         print("  •", name)
# import cv2

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# if not cap.isOpened():
#     print("Camera at index 0 is not accessible.")
# else:
#     print("Press ESC to close camera window.")
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
#         cv2.imshow("Camera Test - Index 0", frame)
#         if cv2.waitKey(1) & 0xFF == 27:  # ESC key
#             break
#     cap.release()
#     cv2.destroyAllWindows()

# import cv2

# def test_multiple_cameras(max_devices=5):
#     for index in range(max_devices):
#         cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
#         if not cap.isOpened():
#             print(f"❌ Camera at index {index} not available.")
#             continue
#         print(f"✅ Testing camera at index {index}. Press ESC to close this one.")

#         while True:
#             ret, frame = cap.read()
#             if not ret:
#                 break
#             cv2.imshow(f"Camera at Index {index}", frame)
#             if cv2.waitKey(1) & 0xFF == 27:  # ESC key to close window
#                 break

#         cap.release()
#         cv2.destroyAllWindows()

# if __name__ == "__main__":
#     test_multiple_cameras()


# import cv2

# def scan_360_camera(max_devices=6):
#     for i in range(max_devices):
#         print(f"🔍 Checking camera index: {i}")
#         cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
#         if cap.isOpened():
#             print(f"✅ Camera at index {i} is available. Press ESC to close.")
#             while True:
#                 ret, frame = cap.read()
#                 if not ret:
#                     print("⚠️ Couldn't read frame.")
#                     break
#                 cv2.imshow(f"Camera {i}", frame)
#                 if cv2.waitKey(1) & 0xFF == 27:  # ESC key
#                     break
#             cap.release()
#             cv2.destroyAllWindows()
#         else:
#             print(f"❌ No camera found at index {i}")

# if __name__ == "__main__":
#     scan_360_camera()


# import sys
# import cv2
# import freenect
# import numpy as np
# from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
# from PyQt5.QtGui import QPixmap, QImage
# from PyQt5.QtCore import QTimer

# class KinectViewer(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Kinect v1 Camera Feed")
#         self.video_label = QLabel("Loading Kinect feed...")
#         layout = QVBoxLayout()
#         layout.addWidget(self.video_label)
#         self.setLayout(layout)

#         self.timer = QTimer()
#         self.timer.timeout.connect(self.update_frame)
#         self.timer.start(30)

#     def update_frame(self):
#         frame, _ = freenect.sync_get_video()
#         if frame is not None:
#             frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
#             image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
#             pixmap = QPixmap.fromImage(image)
#             self.video_label.setPixmap(pixmap)
#             self.video_label.setScaledContents(True)

#     def closeEvent(self, event):
#         freenect.sync_stop()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     viewer = KinectViewer()
#     viewer.show()
#     sys.exit(app.exec_())
import cv2

def find_kinect():
    for index in range(5):  # Try 0–4
        cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
        if cap.isOpened():
            print(f"✅ Camera found at index {index}")
            ret, frame = cap.read()
            if ret:
                cv2.imshow(f"Camera {index}", frame)
                print("Press ESC to close.")
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    cv2.imshow(f"Camera {index}", frame)
                    if cv2.waitKey(1) & 0xFF == 27:
                        break
            cap.release()
            cv2.destroyAllWindows()
        else:
            print(f"❌ No camera at index {index}")

find_kinect()
