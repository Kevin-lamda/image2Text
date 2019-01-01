#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import pytesseract
from PIL import Image, ImageFont, ImageDraw
vcode=pytesseract.image_to_string(Image.open("1.jpg"))   
print(vcode)
