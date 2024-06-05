import ultralytics
import os
ultralytics.checks()


# main code to run YOLO training
from ultralytics import YOLO

infer = YOLO("C:\\MASTER\\runs\\detect\\train12\\weights\\best.pt")

# List of image paths
#image_paths = ["C:\\MASTER\\Testbilder\\lidar\\B8 Lidar knots zoom 2.png"]  # Add more paths as needed

image_dir = "C:\\MASTER\\Testbilder\\lidar"

# Predict and save each image
for filename in os.listdir(image_dir):
    image_path = os.path.join(image_dir, filename)
    result = infer.predict(image_path, save=True)
    print("Processed:", image_path)
    # Save results to the output directory if needed
    # This step depends on how `predict` returns the result; adjust accordingly
