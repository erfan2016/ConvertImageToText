import cv2
import pytesseract

imgPath = 'img.jpg'
pytesseract.pytesseract.tesseract_cmd = r'[path]\Tesseract-OCR\tesseract.exe'
image  = cv2.imread(imgPath)
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
string = pytesseract.image_to_string(gray_img, lang='fas')
print(string)