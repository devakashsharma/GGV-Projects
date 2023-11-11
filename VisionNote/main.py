# Import necessary modules
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Initialize YOLO v3 with its weights, configuration, and class names
yolo = cv2.dnn.readNet("path/to/yolov3-tiny.weights", "path/to/yolov3-tiny.cfg")
classes = []
with open("path/to/coco.names") as f:
    classes = f.read().splitlines()

# Load the image you want to detect (change the path as per your image)
image = cv2.imread("path/to/your/image.jpg")

# Prepare the image for YOLO input
blob = cv2.dnn.blobFromImage(image, 1/255, (320, 320), (0, 0, 0), swapRB=True, crop=False)

# Reshape the blob and convert from BGR to RGB
i = blob[0].reshape(320, 320, 3)
i = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)

# Set the input for YOLO
yolo.setInput(blob)

# Get the output layer names
output_layers_name = yolo.getUnconnectedOutLayersNames()

# Forward pass through YOLO
Layeroutput = yolo.forward(output_layers_name)

# Initialize lists for bounding boxes, confidences, and class IDs
boxes = []
confidences = []
class_ids = []

# Get the image dimensions
width, height = image.shape[1], image.shape[0]

# Process YOLO detections
for detection in output:
    scores = detection[5:]
    class_id = np.argmax(scores)
    confidence = scores[class_id]

    if confidence > 0.7:
        center_x = int(detection[0] * width)
        center_y = int(detection[1] * height)
        w = int(detection[2] * width)
        h = int(detection[3] * height)

        x = int(center_x - w / 2)
        y = int(center_y - h / 2)

        boxes.append([x, y, w, h])
        confidences.append(float(confidence))
        class_ids.append(class_id)

# len(boxes)

# Apply non-maximum suppression to filter out overlapping detections
indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

# Set font and generate random colors for bounding boxes
font = cv2.FONT_HERSHEY_PLAIN
colors = np.random.uniform(0, 255, size = (len(boxes), 3))

# Draw bounding boxes and labels on the image
if len(indexes) > 0:
  for i in indexes.flatten():
    x,y,w,h = boxes[i]

    label = str(classes[class_ids[i]])
    confi = str(round(confidences[i], 2))
    color = colors[i]

    cv2.rectangle(image, (x, y), (x+w, y+h), color, 2)
    # cv2.putText(image, label + " " + confi, (x, y+20), font, (255, 255, 255), 2)
    cv2.putText(image, label + " " + confi, (x, y + 20), font, 1.0, (255, 255, 255), 2)

# Display the image with bounding boxes
plt.imshow(image)
plt.show()