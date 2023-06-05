import cv2
from Funcao1 import *
from warning_green import *

atual = -1; past = -1

if __name__ == "__main__":
    camera = cv2.VideoCapture(0)
    validation, frame = camera.read()

    while validation:
        validation, frame = camera.read()
        resultado, mascara = mask_apply(frame)

        contours, hierarchy = cv2.findContours(mascara.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        lower_bound = np.array([20, 80, 80])	 
        upper_bound = np.array([30, 255, 255])
        output = cv2.drawContours(resultado, contours, -1, (0, 0, 255), 3)
        atual = warning_green(mascara)
        cv2.imshow("Cubos hsv", resultado)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        if past != atual and atual:
            print("apareceu verde") 
        past = atual

    cv2.waitKey(0)
    cv2.destroyAllWindows()
