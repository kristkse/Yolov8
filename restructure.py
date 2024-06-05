import os
import shutil
import random

# Paths for the source and destination directories
source_dir = 'C:\\MASTER\\Images resized'
destination_dir = 'C:\\MASTER\\Images resized 4'

# Ensure the destination directory exists
os.makedirs(destination_dir, exist_ok=True)

# List all image files in the source directory
all_images = [file for file in os.listdir(source_dir) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]

# Ensure there are enough images to select
if len(all_images) < 4000:
    raise ValueError("Not enough images to select 4000 unique items.")

# Randomly select 4000 images
selected_images = random.sample(all_images, 4000)

# Copy the selected images to the destination directory
for image in selected_images:
    src_path = os.path.join(source_dir, image)
    dst_path = os.path.join(destination_dir, image)
    shutil.copy2(src_path, dst_path)  # Use copy2 to preserve metadata

print("4000 images have been randomly selected and copied.")
