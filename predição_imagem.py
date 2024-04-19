import os
import cv2
from matplotlib import pyplot as plt
from ultralytics import YOLO
import numpy

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

# load a pretrained YOLOv8n model
model_path = os.path.join('.', 'best (3).pt')
model = YOLO(model_path)  

# predict on an image
detection_output = model.predict(source="images/20230526_122824.jpg", conf=0.1, save=True)

def mostrar(img):
    fig = plt.gcf()
    fig.set_size_inches(16, 10)
    plt.axis('off')
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()

dir_predicoes = 'runs/detect/predict17'
caminhos = [os.path.join(dir_predicoes, nome) for nome in os.listdir(dir_predicoes)]
for caminho_imagem in caminhos:
    imagem = cv2.imread(caminho_imagem)
    mostrar(imagem)

# Display tensor array
print(detection_output)

# Display numpy array
print(detection_output[0].numpy())