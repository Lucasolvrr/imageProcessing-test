import cv2

# Carregar imagem
image = cv2.imread('images/image.jpg')

# Aplicar filtro gaussiano
blurred = cv2.GaussianBlur(image, (5, 5), 5)  

# Mostrar imagens
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)    
cv2.namedWindow('Suavizada (Gaussiano)', cv2.WINDOW_NORMAL)    

cv2.imshow('Original', image)
cv2.imshow('Suavizada (Gaussiano)', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
