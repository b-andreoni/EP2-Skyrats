import cv2
import numpy as np

# Leitura da imagem
imagem = cv2.imread('imagens/cubos_praia.jpeg', -1)

hsv = cv2.cvtColor (imagem, cv2.COLOR_BGR2HSV)

lower_verde = np.array([50, 100, 20])
upper_verde = np.array([80, 255, 255])

mascara = cv2.inRange(hsv, lower_verde, upper_verde)

# Remover ruido
#define kernel size  
kernel = np.ones((7,7),np.uint8)

mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel)
mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)

resultado = cv2.bitwise_and(imagem, imagem, mask=mascara)

# Mostrar imagem

cv2.imshow("Cubos hsv", resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()