#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 08:35:27 2019

@author: rehan
"""

from PIL import Image
import os 
import numpy
import sys

SIZE = 128, 128
IMAGEPATH = 'input.jpg'

img = Image.open(IMAGEPATH).convert('LA')
img.thumbnail(SIZE, Image.ANTIALIAS)
np_im = numpy.array(img)


txtOut = open('output.txt','w+')

ans=""
for j in range(0,len(np_im)):
    for i in range(0,len(np_im[0])):
        
        if list(np_im[j,i])[0]>127.5:
            ans=ans+str(0)
        else:
            ans=ans+str(1)
    ans=ans+'\n'

txtOut.write(ans)
txtOut.close()
