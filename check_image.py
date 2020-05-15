from PIL import Image
import pytesseract
  
img = Image.open('res/20120282OLnL2ubF9j.jpg')
text = pytesseract.image_to_string(img, lang='chi_tra')
print(text)
