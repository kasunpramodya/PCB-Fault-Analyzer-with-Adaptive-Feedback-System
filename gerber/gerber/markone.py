import cv2
import re

def extract_coordinates_and_units(gerber_file):
    coordinates = []
    units = "unknown"

    with open(gerber_file) as file:
        for line in file:
            # Check for units declaration
            if "G70" in line or "%MOIN" in line:
                units = "inches"
            elif "G71" in line or "%MOMM" in line:
                units = "millimeters"
            
            # Match X and Y coordinates
            x_match = re.search(r'X(-?\d+)', line)
            y_match = re.search(r'Y(-?\d+)', line)
            
            if x_match and y_match:
                x = float(x_match.group(1))
                y = float(y_match.group(1))
                coordinates.append((x, y))
    
    return coordinates, units

# Extract coordinates from Gerber file
gerber_file_path = r'F:\qtdesigner\gerber\gerber\test.gbr'
coords, units = extract_coordinates_and_units(gerber_file_path)

# Load the image
image_path = r'F:\qtdesigner\test3fcumask.jpg'
image = cv2.imread(image_path)

# Convert the coordinate system if needed (e.g., flip Y-axis)
height, width, _ = image.shape

# Determine scaling factors based on the max and min coordinate values
max_x = max([x for x, y in coords])
max_y = max([y for x, y in coords])
min_x = min([x for x, y in coords])
min_y = min([y for x, y in coords])

# Calculate the range
range_x = max_x - min_x
range_y = max_y - min_y

# Mark each normalized coordinate with a red dot
color = (0, 0, 255)  # Red color in BGR
thickness = -1  # Solid fill
radius = 5  # Radius of the dot

for coord in coords:
    x, y = coord
    # Normalize coordinates
    norm_x = (x - min_x) / range_x * width
    norm_y = (y - min_y) / range_y * height
    
    # Adjust for image coordinate system
    x = int(norm_x)
    y = int(height - norm_y)  # Flip Y-axis
    
    if 0 <= x < width and 0 <= y < height:
        image = cv2.circle(image, (x, y), radius, color, thickness)

# Save the result
output_path = r'F:\qtdesigner\gerber\test3_marked_all.jpg'
cv2.imwrite(output_path, image)

# Display the image
cv2.imshow('Image with Marked Coordinates', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
