import cv2

# Carregar o classificador pré-treinado para detecção de rostos
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Carregar a imagem
image = cv2.imread('images/people.jpg')

# Converter a imagem para escala de cinza (a detecção de rostos é realizada em imagens em escala de cinza)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detectar rostos na imagem
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Desenhar retângulos ao redor dos rostos detectados
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Exibir a imagem com os rostos detectados
cv2.imshow('Rostos detectados', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
