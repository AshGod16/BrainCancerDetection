from PIL import Image
import io
import base64

def encode_image_to_base64(image):
    if len(image.shape) == 2:  # Grayscale
        image = Image.fromarray(image)
    else:  # RGB or RGBA
        image = Image.fromarray(image, 'RGB')

    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return img_str