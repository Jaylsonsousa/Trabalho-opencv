import cv2

# Carregar a imagem
image = cv2.imread('loboguara-cke.webp', 0)  # Carregar em escala de cinza

# Aplicar detecção de bordas com o algoritmo Canny
edges = cv2.Canny(image, 100, 200)

# Exibir a imagem resultante
cv2.imshow('Detecção de Bordas com Canny', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
