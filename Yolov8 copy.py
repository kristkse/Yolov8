import ultralytics
import os
ultralytics.checks()


# main code to run YOLO training
from ultralytics import YOLO

# Load a model
#model = YOLO("yolov8n.yaml")  # build a new model from scratch
#model = YOLO("yolov8n.pt")     # load a pretrained model (recommended for training)
model = YOLO("C:\\MASTER\\runs\\detect\\train11\\weights\\best.pt")


# Use the model
#results = model.train(data="knots.yaml", epochs=40, pretrained=True, iou=0.5, visualize=True, patience=0, augment=True)  # train the model
results = model.train(data="knots.yaml", 
                      epochs=20,  # Adjusted number of epochs for continued training
                      lr0 = 0.001,
                      pretrained=True,  # This continues training from the loaded weights
                      iou=0.5, 
                      visualize=True, 
                      patience=3,  # Example: Use patience to prevent overfitting
                      augment=True)
results = model.val()  # evaluate model performance
