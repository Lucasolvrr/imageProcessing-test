import cv2

# Carregar imagem
image = cv2.imread('images/image.jpg')

# Aplicar filtro de suavização (blur)
blurred = cv2.blur(image, (5, 5))  # kernel de 5x5

# Mostrar imagens
cv2.imshow('Original', image)
cv2.imshow('Suavizada', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
