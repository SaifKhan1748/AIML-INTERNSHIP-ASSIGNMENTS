import cv2
import matplotlib.pyplot as plt

# Load image
image = cv2.imread("sample.jpg")

# Convert to RGB (for display)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 1. Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 2. Blur
blur = cv2.GaussianBlur(image_rgb, (7, 7), 0)

# 3. Edge Detection
edges = cv2.Canny(gray, 100, 200)

# Display all images
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(blur)
plt.title("Blurred Image")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(edges, cmap='gray')
plt.title("Edge Detection")
plt.axis("off")

plt.tight_layout()
plt.show()