# pip install opencv-python
import cv2

# Carrega modelo.
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Carrega imagem.
img = cv2.imread('bah.jpg')

# Converte para escala em cinza.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detecta rostos.
faces = faceCascade.detectMultiScale(gray, 1.1, 4)

# Desenha retângulo no rosto detectado.
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
# Mostra resultado.
cv2.imshow('img', img)
cv2.waitKey()