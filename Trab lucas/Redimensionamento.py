import cv2

# Carregar a imagem
image = cv2.imread('loboguara-cke.webp')

# Redimensionar a imagem para 200x200
resized_image = cv2.resize(image, (200, 200))

# Exibir a imagem redimensionada
cv2.imshow('Imagem Redimensionada', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
