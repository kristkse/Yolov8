import os
import cv2

def downsample_images(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # Loop through each image and downsample
    for image_file in image_files:
        input_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, image_file)

        # Read the image
        image = cv2.imread(input_path)

        # Check if the image is not None (i.e., it was successfully read)
        if image is not None:
            # Get the original dimensions
            height, width = image.shape[:2]

            # Downsample to 1/4 of the original size
            downsampled_image = cv2.resize(image, (width // 4, height // 4))

            # Save the downsampled image
            cv2.imwrite(output_path, downsampled_image)

            print(f"Downsampled {image_file} and saved to {output_path}")

input_folder = "C:\\MASTER\\KnotsData"
output_folder = "C:\\MASTER\\KnotsData resized"

downsample_images(input_folder, output_folder)
