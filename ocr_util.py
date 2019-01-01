#!/usr/bin/env python3
#-*- coding: UTF-8 -*- 
from aip import AipOcr
import cv2
import threshold_util
from pytesseract import *
from PIL import Image
from PIL import ImageEnhance

# 认证信息
APP_ID = '15315796'
API_KEY = 'xQEaQ1C4G4Gm9VMEE6p6QGDF'
SECRET_KEY = 'mKQd8iPzdASUZYeNHfvOAgP6riWuiBBP'


def get_ocr_str(file_path, origin_format=True):
    file_path = threshold_util.threshold(file_path)
    """
    图片转文字
    :param file_path: 图片路径
    :return:
    """
    with open(file_path, 'rb') as fp:
        file_bytes = fp.read()

    return get_ocr_str_from_bytes(file_bytes, origin_format)


def get_ocr_str_from_bytes(file_bytes, origin_format=True): 
    #tesseract识别
    if 1==1:
        
        return pytesseract.image_to_string(image)
    #百度 OCR
    else:
        ocr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        options = {
            'detect_direction': 'false',
            'language_type': 'ENG',
        }
        result_dict = ocr.basicAccurate(file_bytes,options)
        if origin_format:
            result_str = '\n'.join([entity['words'] for entity in result_dict['words_result']])
        else:
            result_str = ''.join([entity['words'] for entity in result_dict['words_result']])
        return result_str


if __name__ == '__main__':
    IMAGE_PATH = "23.jpeg"
    print(get_ocr_str(IMAGE_PATH))
