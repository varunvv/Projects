import cv2
import numpy as np

def adjust_brightness(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #convert it to hsv
    h, s, v = cv2.split(hsv)
    x = v - v*.65
    x = x.astype('uint8')
    final_hsv = cv2.merge((h, s, x))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img
    #cv2.imwrite("image_processed.jpg", img)
def adjust_hue(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #convert it to hsv
    h, s, v = cv2.split(hsv)
    x = h - h *.5
    x = x.astype('uint8')
    final_hsv = cv2.merge((x, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img
    #cv2.imwrite("image_processed.jpg", img)

def adjust_saturation(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #convert it to hsv
    h, s, v = cv2.split(hsv)
    x = s - s *.5
    x = x.astype('uint8')
    final_hsv = cv2.merge((h, x, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img
    #cv2.imwrite("image_processed.jpg", img)

def adjust_gamma(image, gamma=1.0):

   invGamma = 1.0 / gamma
   table = np.array([((i / 255.0) ** invGamma) * 255
      for i in np.arange(0, 256)]).astype("uint8")
   
   return cv2.LUT(image, table)

def custom_adjust(img):
    h,w,_ = np.shape(img)
    print h,w




pimg = cv2.imread('7.png', 1)
cv2.imshow('original',pimg)

# pimg = adjust_brightness(original)
# cv2.imshow("brightness reduced", pimg)

# #pimg = adjust_hue(pimg)

# #pimg = adjust_saturation(pimg)

# gamma = .4
# pimg = adjust_gamma(pimg, gamma=gamma)
# cv2.imshow("gammam image 1", pimg)

pimg = custom_adjust(pimg)

cv2.waitKey(0)
cv2.destroyAllWindows()
