import albumentations as A
import cv2

def load_bboxes_and_labels(filepath):
    bboxes = []
    labels = []
    with open(filepath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split()
            labels.append(int(parts[0]))  # Class label
            bbox = [float(x) for x in parts[1:5]]  # Bounding box coordinates
            bboxes.append(bbox)
    return bboxes, labels

transform = A.Compose([A.HorizontalFlip(p=0.8),
                        A.VerticalFlip(p=0.5),    
                        A.RandomBrightnessContrast(brightness_limit=0.6, contrast_limit=0.75, p=0.5),
                        A.HueSaturationValue(hue_shift_limit=20, sat_shift_limit=30, val_shift_limit=20, p=0.5),
                        A.Perspective(scale=(0.01, 0.05), p=0.5),
                        A.ShiftScaleRotate(shift_limit=0.1, scale_limit=0.2, rotate_limit=10, p=1.0, border_mode=cv2.BORDER_REFLECT)],
                        bbox_params = A.BboxParams(format='yolo', label_fields=['class_labels']))


image_path = 'train\\images\\106600051.bmp'
label_path = 'train\\labels\\106600051.txt'
bboxes, labels = load_bboxes_and_labels(label_path)


image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 

transformed = transform(image = image , bboxes= bboxes, class_labels = labels)
transformed_image = transformed['image']
transformed_bboxes = transformed['bboxes']

transformed_image = cv2.cvtColor(transformed_image, cv2.COLOR_RGB2BGR)

# Save the transformed image
cv2.imwrite('transformed_image.bmp', transformed_image) 

# Output the transformed bounding boxes to check correctness
print(transformed_bboxes)
prin(labels)