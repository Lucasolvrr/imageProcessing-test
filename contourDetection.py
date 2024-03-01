import cv2
import numpy as np

# Carregar imagem em escala de cinza
image = cv2.imread('images/image.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar uma operação de limiarização para binarizar a imagem
_, thresholded = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Encontrar contornos na imagem binarizada
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Desenhar os contornos na imagem original
contour_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

# Exibir a imagem com os contornos
cv2.imshow('Contornos', contour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
