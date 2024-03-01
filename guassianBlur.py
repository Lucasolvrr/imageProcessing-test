import cv2

# Carregar imagem
image = cv2.imread('images/image.jpg')

# Aplicar filtro gaussiano
blurred = cv2.GaussianBlur(image, (5, 5), 0)  # kernel de 5x5, desvio padrão 0

# Mostrar imagens
cv2.imshow('Original', image)
cv2.imshow('Suavizada (Gaussiano)', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
