import pytesseract
from PIL import Image

img_path = "testeocr3.jpg"

img = Image.open(img_path)

text = pytesseract.image_to_string(img)
print(f"Extracted text: {text}")
