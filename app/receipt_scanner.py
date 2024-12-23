import pytesseract
from PIL import Image

def extract_text_from_image(image_path):
    """Extract text from a receipt image using Tesseract."""
    img = Image.open(image_path)
    return pytesseract.image_to_string(img)
