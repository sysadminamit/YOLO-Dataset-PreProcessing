# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 01:01:05 2018

@author: Nilagnik
"""

import cv2
import numpy as np
import glob
import os

input_images = glob.glob('C:/Users/ADMIN/Desktop/CU Project/data/*')
output_folder = 'C:/Users/ADMIN/Desktop/CU Project/output'
if not os.path.isdir(output_folder):
    os.makedirs(output_folder)

for i, j in enumerate(input_images):

    image = cv2.imread(j)
    image=cv2.resize(image,(416, 416))
    os.chdir(output_folder)
    out = str(i) + '.jpg'
    cv2.imwrite(out, image)
    os.chdir("../")
    
