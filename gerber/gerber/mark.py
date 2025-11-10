import cv2

# Load the image
image_path = r'F:\qtdesigner\gerber\test3_markedoo.jpg'
image = cv2.imread(image_path)

# Example coordinate (X, Y) from your list
# These coordinates are probably too large, so we need to scale them down
x, y = 10160000.0, -6379000.0  # Example coordinates

# Scaling factor, assuming coordinates are in hundredths of millimeters
scaling_factor = 10000.0

# Adjust the coordinate system if needed (e.g., flip Y-axis)
height, width, _ = image.shape
x = x / scaling_factor
y = height - (abs(y) / scaling_factor)  # Adjust the coordinate scaling and flip the Y-axis

# Convert to integer pixel positions
x = int(x)
y = int(y)

# Check if coordinates are within the image boundaries
if 0 <= x < width and 0 <= y < height:
    # Mark the coordinate with a red dot
    color = (0, 0, 255)  # Red color in BGR
    thickness = -1  # Solid fill
    radius = 5  # Radius of the dot
    image = cv2.circle(image, (x, y), radius, color, thickness)
else:
    print("Coordinates are out of image bounds")

# Save the result
output_path = r'F:\qtdesigner\gerber\test3_markedooo.jpg'
cv2.imwrite(output_path, image)

# Display the image
cv2.imshow('Image with Marked Coordinate', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
