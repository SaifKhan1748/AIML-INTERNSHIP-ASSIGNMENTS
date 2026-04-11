import cv2
import matplotlib.pyplot as plt

# Load image
image = cv2.imread("sample.jpg")

# Convert BGR to RGB (for correct display)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Print shape
print("Image Shape:", image.shape)

# Print number of channels
if len(image.shape) == 3:
    print("Channels:", image.shape[2])
else:
    print("Grayscale Image (1 channel)")

# Print pixel values (first 5 pixels)
print("\nSample Pixel Values (first 5 pixels):")
print(image[0][0:5])

# Display image
plt.imshow(image_rgb)
plt.title("Loaded Image")
plt.axis("off")
plt.show()