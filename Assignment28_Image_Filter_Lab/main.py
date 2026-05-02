import cv2
import numpy as np
from PIL import Image

# First, check if sample.jpg exists, if not create one
try:
    img = cv2.imread("sample.jpg")
    if img is None:
        raise FileNotFoundError
except:
    print("📌 Creating sample.jpg...")
    # Create a sample image with gradient
    sample_array = np.zeros((200, 200, 3), dtype=np.uint8)
    for i in range(200):
        for j in range(200):
            sample_array[i, j] = [i * 1.27, j * 1.27, 128]
    cv2.imwrite("sample.jpg", sample_array)
    img = cv2.imread("sample.jpg")
    print("✅ sample.jpg created\n")

# Check if image loaded
if img is None:
    print("Error: Image not found!")
    exit()

print("✅ Image loaded successfully!")
print(f"📌 Image shape: {img.shape}")

# -----------------------------
# GRAYSCALE
# -----------------------------
print("\n📌 Converting to Grayscale...")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("grayscale_output.jpg", gray)
print("✅ Grayscale image saved as 'grayscale_output.jpg'")

# -----------------------------
# BLUR
# -----------------------------
print("\n📌 Applying Gaussian Blur...")
blur = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imwrite("blur_output.jpg", blur)
print("✅ Blurred image saved as 'blur_output.jpg'")

# Strong blur
blur_strong = cv2.GaussianBlur(img, (15, 15), 0)
cv2.imwrite("blur_strong_output.jpg", blur_strong)
print("✅ Strong blurred image saved as 'blur_strong_output.jpg'")

# -----------------------------
# EDGE DETECTION
# -----------------------------
print("\n📌 Applying Edge Detection (Canny)...")
edges = cv2.Canny(gray, 100, 200)
cv2.imwrite("edges_output.jpg", edges)
print("✅ Edge detection image saved as 'edges_output.jpg'")

# Sobel edge detection
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
sobel = np.sqrt(sobelx**2 + sobely**2).astype(np.uint8)
cv2.imwrite("sobel_output.jpg", sobel)
print("✅ Sobel edge detection saved as 'sobel_output.jpg'")

# Laplacian edge detection
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))
cv2.imwrite("laplacian_output.jpg", laplacian)
print("✅ Laplacian edge detection saved as 'laplacian_output.jpg'")

# -----------------------------
# MORPHOLOGICAL OPERATIONS
# -----------------------------
print("\n📌 Applying Morphological Operations...")
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# Erosion
erosion = cv2.erode(edges, kernel, iterations=1)
cv2.imwrite("erosion_output.jpg", erosion)
print("✅ Erosion image saved as 'erosion_output.jpg'")

# Dilation
dilation = cv2.dilate(edges, kernel, iterations=1)
cv2.imwrite("dilation_output.jpg", dilation)
print("✅ Dilation image saved as 'dilation_output.jpg'")

# Opening (erosion followed by dilation)
opening = cv2.morphologyEx(edges, cv2.MORPH_OPEN, kernel)
cv2.imwrite("opening_output.jpg", opening)
print("✅ Opening image saved as 'opening_output.jpg'")

# Closing (dilation followed by erosion)
closing = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
cv2.imwrite("closing_output.jpg", closing)
print("✅ Closing image saved as 'closing_output.jpg'")

# -----------------------------
# THRESHOLDING
# -----------------------------
print("\n📌 Applying Thresholding...")
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite("binary_output.jpg", binary)
print("✅ Binary threshold image saved as 'binary_output.jpg'")

# Adaptive thresholding
adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imwrite("adaptive_threshold_output.jpg", adaptive)
print("✅ Adaptive threshold image saved as 'adaptive_threshold_output.jpg'")

# Otsu's thresholding
ret, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imwrite("otsu_threshold_output.jpg", otsu)
print("✅ Otsu's threshold image saved as 'otsu_threshold_output.jpg'")

# Note: Display windows skipped in headless environment
# Uncomment below to display images in GUI environment:
# print("\n📌 Displaying images...")
# print("Press any key to close each window")
# cv2.imshow("Original Image", img)
# cv2.waitKey(0)
# cv2.imshow("Grayscale Image", gray)
# cv2.waitKey(0)
# cv2.imshow("Blurred Image", blur)
# cv2.waitKey(0)
# cv2.imshow("Edge Detection (Canny)", edges)
# cv2.waitKey(0)
# cv2.imshow("Sobel Edge Detection", sobel)
# cv2.waitKey(0)
# cv2.imshow("Binary Threshold", binary)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

print("\n✅ All operations completed!")
print("\n📌 Output files created:")
print("- grayscale_output.jpg")
print("- blur_output.jpg")
print("- blur_strong_output.jpg")
print("- edges_output.jpg")
print("- sobel_output.jpg")
print("- laplacian_output.jpg")
print("- erosion_output.jpg")
print("- dilation_output.jpg")
print("- opening_output.jpg")
print("- closing_output.jpg")
print("- binary_output.jpg")
print("- adaptive_threshold_output.jpg")
print("- otsu_threshold_output.jpg")
