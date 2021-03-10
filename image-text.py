import cv2
import pytesseract

def imageToText(file):
	pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
	img = cv2.imread(file)
	text = pytesseract.image_to_string(img)	
	return text

if __name__ == "__main__":

	file = "test-save.png"
	text = imageToText(file)
	print(text)
