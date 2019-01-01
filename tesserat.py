#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import pytesseract
from pyocr import pyocr
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'D:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
tessdata_dir_config = '--tessdata-dir "D:/Program Files (x86)/Tesseract-OCR/tessdata"'

image = Image.open("21.png")
code = pytesseract.image_to_string(image, config=tessdata_dir_config)
print(code)

image = Image.open('21.png')
result = pytesseract.image_to_string(image)
print(result)
