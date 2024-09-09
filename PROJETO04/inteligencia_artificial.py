############################ PROJETO 04 ############################

#  - Bibliotecas usadas
# - opencv-python  -  mediapipe  -  cvzone

import cv2
from cvzone.HandTrackingModule import HandDetector

# Rastreamento de movimentos das mãos com captura da tela
webcam = cv2.VideoCapture(0)
rastreador = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    sucesso, imagem = webcam.read()
    coordenadas, imagem_maos = rastreador.findHands(imagem)

    cv2.imshow('Inteligência artificial', imagem)

    if cv2.waitKey(1) != -1:
        break

webcam.release()
cv2.destroyAllWindows()