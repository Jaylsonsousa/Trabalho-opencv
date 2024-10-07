import cv2
import numpy as np

# Carregar a imagem
image = cv2.imread('loboguara-cke.webp')

# Obter as dimensões da imagem
height, width = image.shape[:2]

# Definir a matriz de rotação
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 45, 1)

# Aplicar a rotação na imagem
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

# Exibir a imagem rotacionada
cv2.imshow('Imagem Rotacionada', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
