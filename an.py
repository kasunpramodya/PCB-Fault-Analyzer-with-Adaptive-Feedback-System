# import sys
# from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
#                              QLabel, QProgressBar, QPushButton)
# from PyQt5.QtCore import QTimer, Qt
# from test import MainWindow

# class LoadingScreen(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Loading...")
#         self.setFixedSize(400, 200)
#         self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
        
#         # Central widget
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
        
#         # Layout
#         layout = QVBoxLayout()
#         central_widget.setLayout(layout)
        
#         # Loading label
#         self.loading_label = QLabel("Loading Application...")
#         self.loading_label.setAlignment(Qt.AlignCenter)
#         self.loading_label.setStyleSheet("font-size: 18px;")
#         layout.addWidget(self.loading_label)
        
#         # Progress bar
#         self.progress = QProgressBar()
#         self.progress.setRange(0, 100)
#         self.progress.setValue(0)
#         layout.addWidget(self.progress)
        
#         # Timer for animation
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_progress)
#         self.timer.start(100)  # Update every 100ms for 10 seconds total
        
#         self.counter = 0
        
#     def update_progress(self):
#         self.counter += 1
#         self.progress.setValue(self.counter)
        
#         # Change loading text for variety
#         if self.counter < 30:
#             self.loading_label.setText("Initializing components...")
#         elif self.counter < 60:
#             self.loading_label.setText("Loading resources...")
#         else:
#             self.loading_label.setText("Almost there...")
        
#         if self.counter >= 100:
#             self.timer.stop()
#             self.close()
#             self.show_main_gui()

#     def show_main_gui(self):
#         self.main_gui = MainWindow()
#         self.main_gui.show()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
    
#     # Set Windows 11 style
#     app.setStyle('Fusion')
    
#     # Show loading screen first
#     loading_screen = LoadingScreen()
#     loading_screen.show()
    
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QLabel, QProgressBar, QPushButton, QHBoxLayout)
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap

class LoadingScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Loading...")
        self.setFixedSize(700, 600)  # Increased height for logo
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Add application logo
        self.logo_label = QLabel()
        # Replace "logo.png" with your actual logo file path
        # Hint: Make sure the logo file is in the same directory as your script
        # or provide the full path
        self.logo_pixmap = QPixmap("logo.png").scaled(500, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.logo_label.setPixmap(self.logo_pixmap)
        self.logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.logo_label)
        
        # Loading label
        self.loading_label = QLabel("Loading Application...")
        self.loading_label.setAlignment(Qt.AlignCenter)
        self.loading_label.setStyleSheet("font-size: 18px; margin-top: 20px;")
        layout.addWidget(self.loading_label)
        
        # Progress bar
        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.progress.setValue(0)
        self.progress.setStyleSheet("""
            QProgressBar {
                border: 2px solid grey;
                border-radius: 5px;
                text-align: center;
                height: 20px;
                margin: 10px 20px;
            }
            QProgressBar::chunk {
                background-color: #0078d7;
                width: 10px;
            }
        """)
        layout.addWidget(self.progress)
        
        # App version info (small at bottom)
        version_label = QLabel("My App v1.0")
        version_label.setAlignment(Qt.AlignCenter)
        version_label.setStyleSheet("font-size: 12px; color: #666; margin-top: 20px;")
        layout.addWidget(version_label)
        
        # Timer for animation
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(100)  # Update every 100ms for 10 seconds total
        
        self.counter = 0
        
    def update_progress(self):
        self.counter += 1
        self.progress.setValue(self.counter)
        
        # Change loading text for variety
        if self.counter < 30:
            self.loading_label.setText("Initializing components...")
        elif self.counter < 60:
            self.loading_label.setText("Loading resources...")
        else:
            self.loading_label.setText("Finalizing setup...")
        
        if self.counter >= 100:
            self.timer.stop()
            self.close()
            self.show_main_gui()

    def show_main_gui(self):
        self.main_gui = MainGUI()
        self.main_gui.show()

class MainGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Application")
        self.setGeometry(100, 100, 800, 600)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Header with logo and title
        header = QWidget()
        header_layout = QHBoxLayout()
        header.setLayout(header_layout)
        
        # Logo in header
        logo_label = QLabel()
        logo_pixmap = QPixmap("logo.png").scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label.setPixmap(logo_pixmap)
        header_layout.addWidget(logo_label)
        
        # Title
        title_label = QLabel("My Application")
        title_label.setStyleSheet("font-size: 28px; font-weight: bold;")
        header_layout.addWidget(title_label, 1)  # Allow title to expand
        
        main_layout.addWidget(header)
        
        # App information section
        app_info = QLabel("""
            <div style='text-align: center; margin: 30px;'>
                <h2>About This Application</h2>
                <p style='font-size: 16px; line-height: 1.6;'>
                    Welcome to My Application, a powerful tool designed to demonstrate<br>
                    modern PyQt5 development with sleek loading animations and<br>
                    Windows 11 style interfaces.
                </p>
                <p style='font-size: 14px; margin-top: 20px;'>
                    <b>Version:</b> 1.0.0<br>
                    <b>Developed by:</b> Your Name<br>
                    <b>Company:</b> Your Company<br>
                    <b>Release Date:</b> January 2023
                </p>
            </div>
        """)
        app_info.setStyleSheet("font-size: 14px;")
        main_layout.addWidget(app_info)
        
        # Features section
        features = QLabel("""
            <div style='margin: 20px;'>
                <h3>Key Features:</h3>
                <ul>
                    <li>Modern loading animation with progress tracking</li>
                    <li>Windows 11 style interface</li>
                    <li>Responsive design</li>
                    <li>Customizable components</li>
                </ul>
            </div>
        """)
        main_layout.addWidget(features)
        
        # Button section
        button_layout = QHBoxLayout()
        
        # Sample buttons
        btn_start = QPushButton("Get Started")
        btn_start.setStyleSheet(self.get_button_style())
        btn_start.clicked.connect(self.on_start_click)
        
        btn_about = QPushButton("Learn More")
        btn_about.setStyleSheet(self.get_button_style("#666"))
        
        button_layout.addStretch()
        button_layout.addWidget(btn_start)
        button_layout.addWidget(btn_about)
        button_layout.addStretch()
        
        main_layout.addLayout(button_layout)
        main_layout.addStretch()
        
    def get_button_style(self, color="#0078d7"):
        return f"""
            QPushButton {{
                padding: 10px 20px;
                font-size: 16px;
                background-color: {color};
                color: white;
                border-radius: 5px;
                min-width: 120px;
                margin: 10px;
            }}
            QPushButton:hover {{
                background-color: {'#106ebe' if color == '#0078d7' else '#777'};
            }}
        """
    
    def on_start_click(self):
        print("Let's get started!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Set Windows 11 style
    app.setStyle('Fusion')
    
    # Set modern font
    font = app.font()
    font.setFamily("Segoe UI")  # Windows 11 default font
    app.setFont(font)
    
    # Show loading screen first
    loading_screen = LoadingScreen()
    loading_screen.show()
    
    sys.exit(app.exec_())