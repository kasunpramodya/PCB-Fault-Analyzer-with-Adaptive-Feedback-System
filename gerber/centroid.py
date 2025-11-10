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
                x = float(x_match.group(1)) / 10000.0  # Apply scaling factor
                y = float(y_match.group(1)) / 10000.0  # Apply scaling factor
                coordinates.append((x, y))
    
    return coordinates, units

# Example usage
gerber_file_path = r'F:\qtdesigner\gerber\gerber\test.gbr'
coords, units = extract_coordinates_and_units(gerber_file_path)

# Write to Centroid file
centroid_file_path = r'F:\qtdesigner\gerber\gerber\test.cent'
with open(centroid_file_path, 'w') as f:
    f.write("Reference Designator, X (mm), Y (mm), Rotation, Side\n")
    for i, coord in enumerate(coords):
        f.write(f"C{i+1}, {coord[0]:.4f}, {coord[1]:.4f}, 0.0, top\n")

print(f"Centroid file created at: {centroid_file_path}")
