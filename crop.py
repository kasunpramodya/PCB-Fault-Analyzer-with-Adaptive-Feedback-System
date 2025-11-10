import cv2 as cv
import matplotlib as mp
img=cv.imread(f"F:\qtdesigner\depositphotos_72924869-stock-illustration-green-printed-circuit-board-pcb.jpg")

cv.imshow("Image",img)
cv.waitKey()
cv.destroyAllWindows()
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import numpy as np
import os

class ImageAreaSelector:
    def __init__(self, master, image_path):
        self.master = master
        self.image_path = image_path
        self.image = Image.open(image_path)
        self.tk_image = ImageTk.PhotoImage(self.image)

        self.canvas = tk.Canvas(master, width=self.tk_image.width(), height=self.tk_image.height())
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

        self.rect = None
        self.start_x = None
        self.start_y = None

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_move)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red')

    def on_mouse_move(self, event):
        self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)

    def on_button_release(self, event):
        end_x, end_y = event.x, event.y
        print(f"Selected area: {self.start_x, self.start_y, end_x, end_y}")

        # Crop the image using the selected coordinates
        cv_image = cv2.imread(self.image_path)
        if end_x > self.start_x and end_y > self.start_y:
            cropped_image = cv_image[self.start_y:end_y, self.start_x:end_x]

            # Close the tkinter window before showing the cropped image
            self.master.destroy()

            # Display the cropped image using OpenCV
            cv2.imshow('Cropped Image', cropped_image)
            cv2.imwrite('F:/qtdesigner/cropped_image.jpg', cropped_image)

            cv2.waitKey(0)
            cv2.destroyAllWindows()

        else:
            print("Invalid selection. Please select a proper area of the image.")

if __name__ == "__main__":
    root = tk.Tk()
    selector = ImageAreaSelector(root, "")  # Use your image path here
    root.mainloop()
# import fitz

# print(fitz.__version__)
# from pdf2image import convert_from_path

# poppler_path = r"D:\Release-24.08.0-0\poppler-24.08.0\Library\bin"
# pages = convert_from_path("example.pdf", 300, poppler_path=poppler_path)
# pages[0].save("example.png", "PNG")

# from cameraproperties import *
# MainWindow()