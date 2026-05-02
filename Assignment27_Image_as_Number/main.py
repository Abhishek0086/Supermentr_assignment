from PIL import Image
import numpy as np

# Create a simple image (100x100 pixels with random colors)
print("=== Creating a Random Image ===")
image_array = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
image = Image.fromarray(image_array)
image.save("random_image.png")
print("✅ Random image created and saved as 'random_image.png'")

# Load the image and convert to array
print("\n=== Loading Image as Array ===")
loaded_image = Image.open("random_image.png")
image_data = np.array(loaded_image)

print(f"Image shape: {image_data.shape}")
print(f"Image dtype: {image_data.dtype}")
print(f"Image size: {loaded_image.size}")

# Display pixel values
print("\n=== First 5x5 Pixel Values (Red Channel) ===")
print(image_data[:5, :5, 0])

# Image statistics
print("\n=== Image Statistics ===")
print(f"Min pixel value: {image_data.min()}")
print(f"Max pixel value: {image_data.max()}")
print(f"Mean pixel value: {image_data.mean():.2f}")
print(f"Std deviation: {image_data.std():.2f}")

# Create a grayscale image
print("\n=== Creating Grayscale Image ===")
grayscale_array = np.random.randint(0, 256, (100, 100), dtype=np.uint8)
grayscale_image = Image.fromarray(grayscale_array, mode='L')
grayscale_image.save("grayscale_image.png")
print("✅ Grayscale image created and saved as 'grayscale_image.png'")

# Modify image using array operations
print("\n=== Modifying Image (Brightness) ===")
brightened = np.clip(image_data * 1.5, 0, 255).astype(np.uint8)
brightened_image = Image.fromarray(brightened)
brightened_image.save("brightened_image.png")
print("✅ Brightened image saved as 'brightened_image.png'")

# Create a gradient image
print("\n=== Creating Gradient Image ===")
gradient = np.zeros((100, 100, 3), dtype=np.uint8)
for i in range(100):
    gradient[i, :] = [i * 2.55, 128, 255 - i * 2.55]
gradient_image = Image.fromarray(gradient)
gradient_image.save("gradient_image.png")
print("✅ Gradient image saved as 'gradient_image.png'")

print("\n=== Summary ===")
print("Images are represented as multi-dimensional NumPy arrays:")
print("- RGB Image: (height, width, 3) - 3 channels for Red, Green, Blue")
print("- Grayscale Image: (height, width) - single channel")
print("- Each pixel value ranges from 0-255")
print("- We can manipulate images by modifying array values")
