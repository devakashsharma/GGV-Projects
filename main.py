# At first we need to import some module
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Now we will set up yolo v3 and it's weight, cfg and we will also add coco name file which is objects names
yolo = cv2.dnn.readNet("C:/Users/soula/Downloads/yolov3-tiny.weights", "C:/Users/soula/Downloads/yolov3-tiny.cfg")
classes = []
with open("C:/Users/soula/Downloads/coco.names") as f:
  classes = f.read().splitlines()

# and now will add our image path which is going to detect

image = cv2.imread("C:/Users/soula/Downloads/bus2.jpg")
# image = cv2.imread("C:/Users/soula/Downloads/smartBus.jpg")
# image = cv2.imread("C:/Users/soula/Downloads/buses.jpg")
# image = cv2.imread("C:/Users/soula/Downloads/car1.jpg")

