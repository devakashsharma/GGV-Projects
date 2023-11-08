# At first we need to import some module
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Now we will set up yolo v3 and it's weight, cfg and we will also add coco name file which is objects names
yolo = cv2.dnn.readNet("C:/Users/soula/Downloads/yolov3-tiny.weights", "C:/Users/soula/Downloads/yolov3-tiny.cfg")
classes = []
with open("C:/Users/soula/Downloads/coco.names") as f:
  classes = f.read().splitlines()

