import cv2

# Carregar a imagem
image = cv2.imread('loboguara-cke.webp')

# Converter a imagem para escala de cinza
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Exibir ambas as imagens
cv2.imshow('Imagem Original', image)
cv2.imshow('Imagem em Escala de Cinza', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
