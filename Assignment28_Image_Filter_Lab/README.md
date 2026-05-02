# Assignment 28: Image Filter Lab

## Overview
A comprehensive image processing laboratory using OpenCV that demonstrates various image filtering and transformation techniques including grayscale conversion, blurring, edge detection, morphological operations, and thresholding.

## What is Image Filtering?
Image filtering is the process of applying mathematical operations to images to enhance, transform, or extract information. Common applications include:
- Noise reduction
- Edge detection
- Image enhancement
- Feature extraction
- Image segmentation

## Requirements
- Python 3.x
- OpenCV library (cv2)
- NumPy library

## Installation
```bash
pip install opencv-python numpy
```

## Usage
```bash
python main.py
```

## Filters and Operations Implemented

### 1. Grayscale Conversion
Converts RGB image to single-channel grayscale
- **Purpose**: Reduce data, simplify processing
- **Output**: `grayscale_output.jpg`

### 2. Gaussian Blur
Smooths image by averaging neighboring pixels
- **Standard blur**: (5, 5) kernel
- **Strong blur**: (15, 15) kernel
- **Purpose**: Noise reduction, smoothing
- **Output**: `blur_output.jpg`, `blur_strong_output.jpg`

### 3. Edge Detection

#### Canny Edge Detection
Multi-stage algorithm for edge detection
- **Thresholds**: 100, 200
- **Purpose**: Detect object boundaries
- **Output**: `edges_output.jpg`

#### Sobel Edge Detection
Gradient-based edge detection
- **Purpose**: Detect edges in X and Y directions
- **Output**: `sobel_output.jpg`

#### Laplacian Edge Detection
Second derivative-based edge detection
- **Purpose**: Detect rapid intensity changes
- **Output**: `laplacian_output.jpg`

### 4. Morphological Operations
Structural transformations on binary images

#### Erosion
Removes small objects and shrinks larger ones
- **Output**: `erosion_output.jpg`

#### Dilation
Expands objects and fills small holes
- **Output**: `dilation_output.jpg`

#### Opening
Erosion followed by dilation (removes small objects)
- **Output**: `opening_output.jpg`

#### Closing
Dilation followed by erosion (fills small holes)
- **Output**: `closing_output.jpg`

### 5. Thresholding
Converts grayscale to binary (black and white)

#### Binary Threshold
Simple threshold at value 127
- **Output**: `binary_output.jpg`

#### Adaptive Threshold
Threshold varies across image
- **Purpose**: Handle varying lighting conditions
- **Output**: `adaptive_threshold_output.jpg`

#### Otsu's Threshold
Automatic threshold calculation
- **Purpose**: Find optimal threshold automatically
- **Output**: `otsu_threshold_output.jpg`

## Output Files
The script generates 13 output images:
1. `grayscale_output.jpg` - Grayscale conversion
2. `blur_output.jpg` - Standard Gaussian blur
3. `blur_strong_output.jpg` - Strong Gaussian blur
4. `edges_output.jpg` - Canny edge detection
5. `sobel_output.jpg` - Sobel edge detection
6. `laplacian_output.jpg` - Laplacian edge detection
7. `erosion_output.jpg` - Morphological erosion
8. `dilation_output.jpg` - Morphological dilation
9. `opening_output.jpg` - Morphological opening
10. `closing_output.jpg` - Morphological closing
11. `binary_output.jpg` - Binary threshold
12. `adaptive_threshold_output.jpg` - Adaptive threshold
13. `otsu_threshold_output.jpg` - Otsu's threshold

## Concepts Covered
- Image filtering fundamentals
- Convolution operations
- Edge detection algorithms
- Morphological operations
- Image thresholding
- Binary image processing
- Computer vision basics

## Common Use Cases

### Noise Reduction
- Gaussian blur
- Bilateral filter
- Median filter

### Edge Detection
- Canny edge detection
- Sobel operator
- Laplacian operator
- Prewitt operator

### Image Segmentation
- Thresholding
- Morphological operations
- Watershed algorithm
- K-means clustering

### Feature Extraction
- Corner detection
- Contour detection
- Histogram analysis
- Template matching

## Real-Life Applications
- Medical image analysis
- Autonomous vehicles
- Quality control in manufacturing
- Document scanning
- Face recognition
- Object detection
- Video surveillance
- Satellite imagery analysis

## OpenCV Functions Used

### Color Space Conversion
```python
cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```

### Blurring
```python
cv2.GaussianBlur(img, (5, 5), 0)
```

### Edge Detection
```python
cv2.Canny(img, 100, 200)
cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
cv2.Laplacian(img, cv2.CV_64F)
```

### Morphological Operations
```python
cv2.erode(img, kernel, iterations=1)
cv2.dilate(img, kernel, iterations=1)
cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
```

### Thresholding
```python
cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
```

## Advanced Topics
- Bilateral filtering
- Median filtering
- Morphological gradients
- Hit-and-miss transforms
- Watershed segmentation
- Contour detection
- Hough transform
- Template matching

## Tips for Image Processing
1. **Preprocessing**: Convert to grayscale, reduce noise
2. **Enhancement**: Adjust contrast, brightness
3. **Segmentation**: Separate objects from background
4. **Feature Extraction**: Identify important features
5. **Post-processing**: Clean up results, remove noise

## Troubleshooting
- **Image not found**: Ensure `sample.jpg` exists in the same directory
- **OpenCV not installed**: Run `pip install opencv-python`
- **Display issues**: Some systems may not support cv2.imshow()

## Practice Exercises
1. Apply multiple filters in sequence
2. Create custom kernels
3. Implement histogram equalization
4. Detect specific colors
5. Track moving objects
6. Combine multiple edge detection methods
7. Create image mosaics
8. Implement image stitching

## Conclusion
Image filtering is a fundamental technique in computer vision and image processing. By understanding and applying various filters, you can:
- Enhance image quality
- Extract meaningful features
- Prepare images for analysis
- Detect objects and patterns
- Build computer vision applications

This lab provides hands-on experience with essential image processing operations used in real-world applications.
