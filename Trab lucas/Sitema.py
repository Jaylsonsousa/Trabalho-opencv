import cv2

# Carregar a imagem
image = cv2.imread('loboguara-cke.webp')

# Exibir a imagem em uma janela
cv2.imshow('Imagem', image)

# Esperar por uma tecla pressionada para fechar a janela
cv2.waitKey(0)
cv2.destroyAllWindows()

