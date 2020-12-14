# I need to apply feature extraction techniques
# should be installed on the server kernel $, pip3 install pytesseract
# on server: apt-get install tesseract-ocr "Not possible" instead =>
# https://towardsdatascience.com/deploy-python-tesseract-ocr-on-heroku-bbcc39391a8d

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd ="/usr/bin/tesseract"

image = Image.open('test.jpeg')
print(pytesseract.image_to_string(image,lang='deu')) # print ocr text from image

