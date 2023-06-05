import cv2
import numpy as np

#

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

# Denhar a borda do quadradinho
# Find contours from the mask

contours, hierarchy = cv2.findContours(mascara.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
lower_bound = np.array([20, 80, 80])	 
upper_bound = np.array([30, 255, 255])
output = cv2.drawContours(resultado, contours, -1, (0, 0, 255), 3)

# Mostrar imagem

cv2.imshow("Cubos hsv", resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()
