# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 16:56:57 2023

@author:大数据204-2020240121-喻春成
"""
import cv2
import numpy as np
img = cv2.imread("2020240121.jpg",1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("src",gray)
dst = cv2.equalizeHist(gray)
cv2.imshow("dst",dst)
cv2.waitKey(0)

