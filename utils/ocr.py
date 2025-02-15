import cv2
import pytesseract
import numpy as np
from PIL import Image

def extract_text_from_image(image):
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    extracted_text = pytesseract.image_to_string(gray)
    return extracted_text.strip()
