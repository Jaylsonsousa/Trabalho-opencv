import cv2
import numpy as np
import tensorflow as tf
from object_detection.utils import visualization_utils as viz_utils

# Carregar o modelo pré-treinado
detection_model = tf.saved_model.load('caminho_para_modelo')

# Carregar e processar a imagem
image = cv2.imread('loboguara-cke.webp')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_tensor = tf.convert_to_tensor(image_rgb)
image_tensor = image_tensor[tf.newaxis, ...]

# Realizar a detecção de objetos
detections = detection_model(image_tensor)

# Visualizar os resultados
image_with_detections = image.copy()
viz_utils.visualize_boxes_and_labels_on_image_array(
    image_with_detections,
    detections['detection_boxes'][0].numpy(),
    detections['detection_classes'][0].numpy().astype(np.int32),
    detections['detection_scores'][0].numpy(),
    category_index,
    use_normalized_coordinates=True,
    max_boxes_to_draw=200,
    min_score_thresh=.30,
    agnostic_mode=False
)

cv2.imshow('Image with Detections', image_with_detections)
cv2.waitKey(0)
cv2.destroyAllWindows()
