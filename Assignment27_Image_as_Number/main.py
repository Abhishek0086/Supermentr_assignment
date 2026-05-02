from PIL import Image
import numpy as np

# First, create a sample image if it doesn't exist
try:
    img = Image.open("sample.jpg")
except FileNotFoundError:
    print("📌 Creating sample.jpg...")
    # Create a sample image with gradient
    sample_array = np.zeros((200, 200, 3), dtype=np.uint8)
    for i in range(200):
        for j in range(200):
            sample_array[i, j] = [i * 1.27, j * 1.27, 128]
    img = Image.fromarray(sample_array)
    img.save("sample.jpg")
    print("✅ sample.jpg created\n")

# Convert to numpy array
img_array = np.array(img)

# -----------------------------
# BASIC INFO
# -----------------------------
print("📌 Image Shape (Height, Width, Channels):", img_array.shape)
print("📌 Data Type:", img_array.dtype)

# -----------------------------
# PIXEL VALUES
# -----------------------------
print("\n📌 Sample Pixel Values (Top-left 3x3 area):")
print(img_array[:3, :3])

# -----------------------------
# CHANNEL INFO
# -----------------------------
if len(img_array.shape) == 3:
    print("\n📌 Number of Channels:", img_array.shape[2])
    print("👉 RGB Channels Explanation:")
    print("Red channel sample:\n", img_array[:3, :3, 0])
    print("Green channel sample:\n", img_array[:3, :3, 1])
    print("Blue channel sample:\n", img_array[:3, :3, 2])
else:
    print("\n📌 Grayscale Image (Single Channel)")

# -----------------------------
# PIXEL RANGE
# -----------------------------
print("\n📌 Pixel Value Range:")
print("Min:", img_array.min())
print("Max:", img_array.max())

# -----------------------------
# IMAGE SIZE
# -----------------------------
height, width = img_array.shape[:2]
print("\n📌 Image Size:")
print("Height:", height)
print("Width:", width)

# -----------------------------
# TOTAL PIXELS
# -----------------------------
print("\n📌 Total Pixels:", height * width)
