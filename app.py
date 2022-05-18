import cv2
import mediapipe as mp

# Inicializar o OpenCV e o mediapipe.
webcam = cv2.VideoCapture(0)
solutionFaceRecognition = mp.solutions.face_detection
faceRecognizer = solutionFaceRecognition.FaceDetection()
draw = mp.solutions.drawing_utils

while True:
    # Ler as informações da wwbcam.
    canRead, img = webcam.read()
    
    if not canRead:
        break
    
    # reconhecer os rostos que tem ali dentro.
    faceList = faceRecognizer.process(img)
    if faceList.detections:
    # desenhar os rostos na imagem.
        for face in faceList.detections:
            draw.draw_detection(img, face)
            
    cv2.imshow("Belos rostos hein", img)
    # Quando apertar ESC, para o loop.
    if cv2.waitKey(5) == 27:
        break
    
webcam.release()
cv2.destroyAllWindows()
