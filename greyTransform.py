import cv2
import numpy as np

img = cv2.imread('images/color-logos.jpg',0)
#img = cv2.imread('logo2.png',0)


cv2.imshow('coloridos.jpg', img)
#cv2.imshow('logo2.png', img)

cv2.waitKey(0)
cv2.destroyAlLWindows()
