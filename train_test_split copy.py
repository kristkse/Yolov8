import os
import random
import shutil

# Set the path to your dataset
dataset_path = 'C:\\MASTER'

# Set the path to the folder containing images and their corresponding labels
images_folder = "C:\\MASTER\\KnotsData resized"
labels_folder = "C:\\MASTER\\knots_labels"

# Set the path to the destination folders
train_folder = os.path.join(dataset_path, 'trainKnots new')
valid_folder = os.path.join(dataset_path, 'validKnots new')

# Create destination folders and subfolders if they don't exist
os.makedirs(os.path.join(train_folder, 'images'), exist_ok=True)
os.makedirs(os.path.join(train_folder, 'labels'), exist_ok=True)
os.makedirs(os.path.join(valid_folder, 'images'), exist_ok=True)
os.makedirs(os.path.join(valid_folder, 'labels'), exist_ok=True)

# Set the percentage of images to move to the validation set
validation_percentage = 20  # Adjust as needed

# Get a list of all image files in the Images folder
image_files = [f for f in os.listdir(images_folder) if f.endswith('.JPG')]

# Calculate the number of images for validation
num_validation_images = int(len(image_files) * (validation_percentage / 100.0))

# Randomly select images for validation
validation_images = random.sample(image_files, num_validation_images)

# Move images and labels to the appropriate folders
for image_file in image_files:
    label_file = image_file.replace('.JPG', '.txt')

    source_image_path = os.path.join(images_folder, image_file)
    source_label_path = os.path.join(labels_folder, label_file)

    if image_file in validation_images:
        destination_folder = valid_folder
    else:
        destination_folder = train_folder

    destination_image_path = os.path.join(destination_folder, 'images', image_file)
    destination_label_path = os.path.join(destination_folder, 'labels', label_file)

    # Move image and label files
    shutil.copy(source_image_path, destination_image_path)
    shutil.copy(source_label_path, destination_label_path)


print("Train, test, split completed.")