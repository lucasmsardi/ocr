import pytesseract
from PIL import Image

# Path to the image inside the container (same directory as ocr.py)
img_path = "testeocr3.jpg"  # The image is directly in the container's /app directory

# Open the image
img = Image.open(img_path)

# Run OCR on the image
text = pytesseract.image_to_string(img)
print(f"Extracted text: {text}")
