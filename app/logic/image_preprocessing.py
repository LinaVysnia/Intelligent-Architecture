import cv2
import numpy as np
from PIL import Image

valid_formats = ['.png', '.jpg', '.jpeg', '.bmp']
def check_accepted_format(file_dir):
    try:
        if file_dir.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            status = "Pass"
            message = f"The file format is suitable"
            return status, message
        raise Exception("The file format is not accepted")
    except Exception as ex:
        status = "Fail"
        message = ex
        return status, message

def check_image_color_mode(img :Image):
    """Checks if an image is RGB or grayscale."""
    try:
        mode = img.mode
        if mode == 'RGB':
            return 'RGB'
        elif mode == 'L':  # 'L' mode represents grayscale
            return 'Grayscale'
        else:
            return f'Other ({mode})'
    except Exception as ex:
        return f"Error: {ex}"
    
def resize(img : Image, size):
    old_size = img.size  # old_size[0] is in (width, height) format

    ratio = float(size[0])/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])
    img.thumbnail(new_size)

    new_im = Image.new("RGB", size, color="white")
    new_im.paste(img, ((size[0]-new_size[0])//2,
                        (size[1]-new_size[1])//2))
    return new_im

def recolour(img : Image):
    img_grey = img.convert('L')
    return img_grey

def pre_process(image_loc, resize = False, new_size = (640, 640), reclr = True, threshold = None):
    """Pre-processes the image. Ensures the format is rgb.
    Args:
        resize = False by default because it's not neccessary for Yolo models as they resize and pad by default . Rescales image and pads if necessary. 
        new_size = tuple(int, int) new size for rescaling. Will only be efefctive if rescale is set to true'
        reclr = True by default. Removes saturation as to not confuse the model. 
        threshold = None or integer between 0 and 255. If not none then when recolourint the image will be thresholded based on the given value
    """

    status, message = check_accepted_format(image_loc)
    #because of the app simplicity and the lack of meaningful UI, I make a choice to stop the program if this fails
    if status == "Fail":
        raise Exception(message) 

    image = Image.open(image_loc)

    if reclr:
        image = recolour(image)
        if threshold:
            image = image.point(lambda x: 255 if x > threshold else 0)

    #converting to rgb if not rgb because the dataset and the model are setup for it
    color_mode = check_image_color_mode(image)
    if color_mode != "RGB":
        image = image.convert("RGB") 

    #stripping auto-rotation
    data = list(image.getdata())
    image_stripped = Image.new(image.mode, image.size)
    image_stripped.putdata(data)
    
    if resize:
        image_stripped = resize(image_stripped, new_size)
    
    return image_stripped