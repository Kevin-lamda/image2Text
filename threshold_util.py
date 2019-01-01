#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import cv2  
import os

def threshold(file_path):
    [dirname,filename] = os.path.split(file_path)
    print(dirname,"\n",filename)
    t_file_path = "t"+filename
    image = cv2.imread(file_path)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  
    cv2.threshold(image, 140, 255, 0, image)  

    #cv2.namedWindow("Image")  
    #cv2.imshow("Image", image)  
    newFile = os.path.join(dirname, t_file_path)
    cv2.imwrite(newFile, image)
    cv2.waitKey(0)
    return os.path.join(dirname,t_file_path)
