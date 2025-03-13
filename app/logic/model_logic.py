from ultralytics import YOLO
from PIL import Image

def get_model_prediction(image_loc, model_link):

    img_test = Image.open(image_loc)
    model = YOLO(model_link)
    results = model.predict(img_test)
    result = results[0].cpu()

    return result
