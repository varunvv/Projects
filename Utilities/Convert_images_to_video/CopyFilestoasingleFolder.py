import os
import numpy as np
import cv2
from os import listdir
from os.path import isfile, join
import scipy
import scipy.misc

parentFolder = '/home/hafx/DNNDataset/Cohn_Kanade_Emotion_Classification/cohn-kanade-images/S058/002_dup/'
inputFile = './output.txt'


outFolderName = './delete/'
if not os.path.exists(outFolderName):
    os.makedirs(outFolderName)
    
count = 1000;   
ptr = open(inputFile,'r')
imgNames = ptr.readlines()
print imgNames
for name in imgNames:
    name = name.strip("\n")
    fullPath = parentFolder + name
    print fullPath
    #a = name.split('.')
    outFullPath = outFolderName + 'test_' +str(count) + '.jpg'
    print outFullPath
    pic = cv2.imread(fullPath,1)
    image = scipy.misc.imresize(pic,(256,256), 'bilinear')

    cv2.imwrite(outFullPath,image)
    count = count + 1

