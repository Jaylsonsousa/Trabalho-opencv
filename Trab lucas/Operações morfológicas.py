import cv2
import numpy as np

# Carregar a imagem
image = cv2.imread('Paisagem_Natural.jfif', 0)  # Carregar como grayscale
cv2.imshow('Imagem Original', image)

# Definir o kernel para as operações morfológicas
kernel = np.ones((3, 3), np.uint8)

# Aplicar Erosão
erosion = cv2.erode(image, kernel, iterations=1)
cv2.imshow('Erosão', erosion)

# Aplicar Dilatação
dilation = cv2.dilate(image, kernel, iterations=1)
cv2.imshow('Dilatação', dilation)

# Aplicar Abertura (Erosão seguida de Dilatação)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow('Abertura', opening)

# Aplicar Fechamento (Dilatação seguida de Erosão)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Fechamento', closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
