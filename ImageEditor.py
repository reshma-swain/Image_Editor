import cv2
import numpy as np

# Callback function for trackbar updates
def update_image(*args):
    # Get trackbar positions
    brightness = cv2.getTrackbarPos('Brightness', 'Image Editor') - 50
    contrast = cv2.getTrackbarPos('Contrast', 'Image Editor') / 50.0
    blur = cv2.getTrackbarPos('Blur', 'Image Editor')

    # Adjust brightness and contrast
    adjusted = cv2.convertScaleAbs(image, alpha=contrast, beta=brightness)


    # Apply Gaussian blur if needed
    if blur > 0:
        adjusted = cv2.GaussianBlur(adjusted, (2 * blur + 1, 2 * blur + 1), 0)

    # Display the updated image
    cv2.imshow('Image Editor', adjusted)

# Load an image
image_path = '/home/asus/Pictures/MOON.jpeg'  # Replace with the path to your image file
image = cv2.imread(image_path)


if image is None:
    print("Error: Unable to load the image. Please check the file path.")
    exit()

# Create a window for the editor
cv2.namedWindow('Image Editor')

# Create trackbars for brightness, contrast, and blur
cv2.createTrackbar('Brightness', 'Image Editor', 50, 100, update_image)
cv2.createTrackbar('Contrast', 'Image Editor', 50, 100, update_image)
cv2.createTrackbar('Blur', 'Image Editor', 0, 10, update_image)

# Initialize the display
update_image()

# Wait until the user presses a key
cv2.waitKey(0)
cv2.destroyAllWindows()
