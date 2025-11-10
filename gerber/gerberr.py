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

# Example usage
gerber_file_path = r'F:\qtdesigner\gerber\gerber\test.gbr'
coords, units = extract_coordinates_and_units(gerber_file_path)

print(f"Units: {units}")
print(f"Total Coordinates: {len(coords)}")
for coord in coords:
    print(f"X: {coord[0]}, Y: {coord[1]}")
