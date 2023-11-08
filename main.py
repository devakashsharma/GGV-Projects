# At first we need to import some module
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Now we will set up yolo v3 and it's weight, cfg and we will also add coco name file which is objects names
yolo = cv2.dnn.readNet("C:/Users/soula/Downloads/yolov3-tiny.weights", "C:/Users/soula/Downloads/yolov3-tiny.cfg")
classes = []
with open("C:/Users/soula/Downloads/coco.names") as f:
  classes = f.read().splitlines()

# and now will add our image path which is going to detect & change the path as per you want

image = cv2.imread("path/to/your/image.jpg")
# image = cv2.imread("path/to/your/image.jpg")
# image = cv2.imread("path/to/your/image.jpg")
# image = cv2.imread("path/to/your/image.jpg")

blob = cv2.dnn.blobFromImage(image, 1/255, (320, 320), (0, 0, 0), swapRB = True, crop = False)

# Reshape & Convert from BGR to RGB
i = blob[0].reshape(320, 320, 3)
i = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)

yolo.setInput(blob)

output_layers_name = yolo.getUnconnectedOutLayersNames()
Layeroutput = yolo.forward(output_layers_name)

boxes = []
confidences = []
class_ids = []
boxes = []
confidences = []
class_ids = []

width, height = image.shape[1], image.shape[0]

for output in Layeroutput:
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

indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
font = cv2.FONT_HERSHEY_PLAIN
colors = np.random.uniform(0, 255, size = (len(boxes), 3))

if len(indexes) > 0:
  for i in indexes.flatten():
    x,y,w,h = boxes[i]

    label = str(classes[class_ids[i]])
    confi = str(round(confidences[i], 2))
    color = colors[i]

    cv2.rectangle(image, (x, y), (x+w, y+h), color, 2)
    # cv2.putText(image, label + " " + confi, (x, y+20), font, (255, 255, 255), 2)
    cv2.putText(image, label + " " + confi, (x, y + 20), font, 1.0, (255, 255, 255), 2)

# showing image
plt.imshow(image)
plt.show()