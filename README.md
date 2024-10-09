OpenCV no Python - README
Introdução
OpenCV é uma biblioteca de visão computacional de código aberto amplamente utilizada para processamento de imagens e vídeos. Este README fornecerá instruções sobre como instalar o OpenCV em Python e como aplicar algumas operações básicas de processamento de imagens.
Instalação do OpenCV em Python
Para instalar o OpenCV em Python, você pode seguir estes passos:
1. Utilize o pip para instalar o pacote opencv-python:
pip install opencv-python
2. Caso precise de recursos extras, como o módulo contrib do OpenCV, você pode instalar o pacote opencv-contrib-python:
pip install opencv-contrib-python
Como Aplicar Operações Básicas com OpenCV em Python
Abaixo estão alguns exemplos de como aplicar operações básicas de processamento de imagens com OpenCV em Python:
Leitura e Exibição de Imagens
import cv2
# Carregar uma imagem
image = cv2.imread('imagem.jpg')
# Exibir a imagem em uma janela
cv2.imshow('Imagem', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
Conversão de Cores
# Carregar uma imagem em tons de cinza
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
Redimensionamento de Imagens
# Redimensionar uma imagem
resized_image = cv2.resize(image, (new_width, new_height))
Detecção de Bordas com o Algoritmo de Canny
# Aplicar detecção de bordas usando o algoritmo de Canny
edges = cv2.Canny(image, threshold1, threshold2)# Trabalho-opencv
