import cv2
import numpy as np
from matplotlib import pyplot as plt

# Carregar imagem em escala de cinza
image = cv2.imread('images/image.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar a Transformada de Fourier
fourier_transform = np.fft.fft2(image)
fourier_spectrum = np.fft.fftshift(fourier_transform)
magnitude_spectrum = 20 * np.log(np.abs(fourier_spectrum))

# Exibir o espectro de frequência
plt.subplot(121), plt.imshow(image, cmap='gray')
plt.title('Imagem de Entrada'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Espectro de Frequência'), plt.xticks([]), plt.yticks([])
plt.show()
