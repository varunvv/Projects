import cv2
import os

inputFolder = "./04delete/"
outputFolder = "./04Resized/"
inputImages = os.listdir(inputFolder)
 
for imgName in inputImages:
	imgPath = inputFolder + imgName
	img = cv2.imread(imgPath);
	resizedImg = cv2.resize(img, (448,448))
	 	
	
	outputImgName = outputFolder + imgName
	cv2.imwrite(outputImgName, resizedImg)

