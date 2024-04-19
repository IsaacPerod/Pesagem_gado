import os
from ultralytics import YOLO

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
results = model.train(data="data.yaml", epochs=100)  # train the model