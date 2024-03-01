import cv2
import numpy as np

# Load image in grayscale
image = cv2.imread('images/notes.jpg', 0)

# Set a threshold value (you can adjust this value)
threshold_value = 127

# Apply binary thresholding
_, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

# Display the original image
cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.imshow('Original Image', image)


# Check if the window exists before resizing
if 'Binary Image' in locals() or 'Binary Image' in globals():
    cv2.destroyWindow('Binary Image')

# Display the binary image
cv2.namedWindow('Binary Image', cv2.WINDOW_NORMAL)
cv2.imshow('Binary Image', binary_image)


cv2.waitKey(0)
cv2.destroyAllWindows()

