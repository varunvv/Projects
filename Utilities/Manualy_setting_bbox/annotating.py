"""
Code will store the cordinates of mouse click 
assumption first click top left corner and second bottom right
in this fasion you can have multiple bounding boxes in an image
"""
# import the necessary packages
import argparse
import numpy as np
import cv2
import time
VideoSource = ".././sample.mp4"
#VideoSource = 0
Des_Folder_Path = "./annotations/"
cap = cv2.VideoCapture(VideoSource)

 
# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
cropping = False
 
def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, cropping
 
    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        #refPt = [(x, y)]
	refPt.append((x, y))	
        cropping = True
 
    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((x, y))
        cropping = False



count = 1;
ret, frame = cap.read()
while(ret):
    # Capture frame-by-frame


    # Display the resulting frame
    file_name = Des_Folder_Path + "frame" + str(count) + ".txt";#annotatin file name
    ofptr = open(file_name,'w')
    #cv2.imshow('frame',frame)
    #cv2.imwrite(file_name,frame);
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_crop)
   
   
    clone = frame.copy()
    refPt = []
    while True:
        # display the image and wait for a keypress
        cv2.imshow("image", frame)
        key = cv2.waitKey(1) & 0xFF
    
        # if the 'r' key is pressed, reset the cropping region
        if key == ord("r"):
            image = clone.copy()
    
        # if the 'c' key is pressed, break from the loop
        elif key == ord("c"):
            break
    print("length of refPt : ",len(refPt));
    for i in range(0,len(refPt),2):
        ofptr.write("0 %f %f %f %f \n" % (refPt[i][0], refPt[i][1], refPt[i+1][0], refPt[i+1][1]))
    count = count+ 1;
   
    ret, frame = cap.read()
    ofptr.close()
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
