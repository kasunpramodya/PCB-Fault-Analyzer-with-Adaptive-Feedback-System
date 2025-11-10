<!-- ========================================================== -->
<!-- 🧠 Kasun Pramodya | Electronics & AI Researcher             -->
<!-- ========================================================== -->

<p align="center">
  <img src="./profile.png" alt="Kasun Pramodya" width="150">
</p>

<h1 align="center">👨‍💻 Vision-Based PCB Fault Analyzer with Adaptive Feedback</h1>
<h3 align="center">⚡ Electronics & AI Researcher | Embedded Vision & Intelligent Systems ⚡</h3>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&duration=2500&pause=800&color=39FF14&center=true&vCenter=true&width=700&lines=🤖+PCB+Fault+Detection;🧠+AI+%2B+Embedded+Systems;🚀+Adaptive+Feedback+Control;📡+Vision-Based+Analysis" alt="Typing SVG" />
</p>

---

## 🚀 Overview

This project is a **Vision-Based PCB Fault Analyzer** that integrates:

- **YOLOv5 / Mask R-CNN** for PCB defect detection  
- **Adaptive Feedback Control** using confidence score to guide precise camera motion  
- **STM32 / microcontroller control** for automated probing  
- Python, PyTorch, OpenCV, and .NET GUI for visualization and operation  

The main entry point is `test.py`.

---

## 🧰 Features

- Detect resistors, capacitors, ICs, diodes, zeners, and other components  
- Adaptive feedback system to improve detection accuracy during live camera scanning  
- Visualization GUI built with **PyQt5** and .NET  
- Support for Gerber file parsing and image-based inspection  
- Cross-platform: Windows and Linux

---

## 📦 Requirements

- Python 3.8+  
- PyTorch  
- OpenCV (`opencv-python`)  
- PyQt5  
- NumPy  
- Pillow  
- Other packages in `requirements.txt`

Install dependencies:

```bash
pip install -r requirements.txt
