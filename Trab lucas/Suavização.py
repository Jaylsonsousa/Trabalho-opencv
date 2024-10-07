import cv2

# Carregar a imagem
image = cv2.imread('loboguara-cke.webp')

# Aplicar o filtro gaussiano para suavizar a imagem
smoothed_image = cv2.GaussianBlur(image, (5, 5), 0)

# Exibir a imagem suavizada
cv2.imshow('Imagem Suavizada', smoothed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
