import cv2

# Lista para armazenar os índices das câmeras
indices = []

# Tente abrir cada índice de 0 a 10
for i in range(10):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f'Câmera encontrada no índice: {i}')
        indices.append(i)
        cap.release()
    else:
        print(f'Nenhuma câmera encontrada no índice: {i}')

print(f'Índices das câmeras: {indices}')