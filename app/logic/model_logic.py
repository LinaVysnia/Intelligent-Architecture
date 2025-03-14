from ultralytics import YOLO
from PIL import Image

def get_model_prediction(image, model_link):

    model = YOLO(model_link)
    results = model.predict(image)
    result = results[0].cpu()

    return result
