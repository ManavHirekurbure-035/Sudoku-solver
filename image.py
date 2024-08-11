from PIL import Image
import pytesseract

# Load the image
image = Image.open('./test1.png')

# Perform OCR
text = pytesseract.image_to_string(image)

print(text)
