import os

# Define class mapping
class_mapping = {
    'Live_Knot': 0,
    'Dead_Knot': 0,  # Assigning same index for all knot-related classes
    'Knot_missing': 2,
    'knot_with_crack': 0,
    'Crack': 4,
    'Quartzity': 5,
    'resin': 6,
    'Marrow': 7,
    'Blue_stain': 8,
    'overgrown': 9
}

# Function to convert bounding box format
def convert_format(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    knots_found = False

    with open(output_file, 'w') as outfile:
        for line in lines:
            line = line.split()
            class_name = line[0]

            # Check if the class is a knot-related class
            if class_name in ['Live_Knot', 'Dead_Knot', 'Knot_missing', 'knot_with_crack']:
                knots_found = True

                # Replace commas with dots for values in the bounding box
                x_min, y_min, x_max, y_max = map(lambda x: float(x.replace(',', '.')), line[1:])

                # Calculate new format values
                x_center = (x_min + x_max) / 2
                y_center = (y_min + y_max) / 2
                width = x_max - x_min
                height = y_max - y_min

                # Write the consolidated knot bounding box
                class_index = class_mapping.get('Live_Knot')  # Use 'Live_Knot' as reference for index
                outfile.write(f"{class_index} {x_center} {y_center} {width} {height}\n")

    # If no knots were found, create an empty file
    if not knots_found:
        open(output_file, 'a').close()

# Specify input and output directories
input_folder = 'Bouding Boxes'
output_folder = 'Bounding Boxes Corrected Only Knots'

# Create output folder if not exists
os.makedirs(output_folder, exist_ok=True)

# Iterate through each file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('_anno.txt'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename.replace('_anno.txt', '.txt'))

        # Perform conversion
        convert_format(input_path, output_path)

print("Conversion completed.")
