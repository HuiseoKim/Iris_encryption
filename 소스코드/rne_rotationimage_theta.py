import numpy as np
import cv2

THETA = [7,45,35,14,43,76,73,0]

def transform(theta):
    img = cv2.imread('croped/Centered_image.png')
    h, w = img.shape[:2]
    M1 = cv2.getRotationMatrix2D((w/2,h/2),theta,1)

    img2=cv2.warpAffine(img,M1, (w,h))

    cv2.imwrite('croped/result'+str(theta)+'.png', img2)

for i in THETA:
    transform(i)
