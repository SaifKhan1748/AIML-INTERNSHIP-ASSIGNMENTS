# 📄 Image as Numbers

# 📌 Overview

This project demonstrates how an image is represented as numerical data in a computer. It loads an image and displays its shape, pixel values, and number of channels, helping to understand the basic concept of image processing.

# 🎯 Features
Load and display an image
Print image shape (height, width, channels)
Display number of channels
Show sample pixel values
Visualize the image using matplotlib

# 🧰 Technologies Used
Python
OpenCV
Matplotlib

# ⚙️ Installation & Setup
1. Install Required Libraries
pip install opencv-python matplotlib
2. Project Structure
image-as-numbers/
│
├── app.py
└── sample.jpg
3. Run the Program
python app.py

# 💡 How It Works
The image is loaded using OpenCV
It is stored as a NumPy array (matrix of numbers)
The shape of the image is printed
Pixel values are accessed directly from the array
The image is displayed using matplotlib

# 📊 Example Output
Image Shape: (224, 224, 3)
Channels: 3

Sample Pixel Values:
[[123 45 67]
 [120 40 60]
 [130 50 70]]

# 🧠 Key Concepts
🔹 Image Representation

An image is stored as a matrix of numbers where each value represents pixel intensity.

🔹 Shape
(height, width, channels)
🔹 Channels
1 → Grayscale
3 → Color (Red, Green, Blue)
🔹 Pixel Values
Range: 0 to 255

# Example:

[123, 45, 67]

# 📌 Outcome

Learned how images are represented numerically and understood basic image properties like shape, channels, and pixel values using Python.