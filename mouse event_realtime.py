import cv2
import numpy as np
# read image
global image,frame,para,rgbh,rgbl,image_h
para=1
frame=cv2.VideoCapture(0)
def mouse_click(event, x, y, flags, param):
    # to check if left mouse
    # button was clicked
    global image,para,rgbl,rgbh
    if event == cv2.EVENT_LBUTTONDOWN:
        para=1
        print("bila",para)
    elif event == cv2.EVENT_RBUTTONDOWN:
        para=2
        print("box",para)
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        para=3
        print("gray")
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        para=4
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        pixel=hsv[y,x]
        print(pixel[0])
        rgbh=np.array([pixel[0]+20,pixel[1]+60,pixel[2]+60])
        rgbl = np.array([pixel[0] -20, pixel[1] -60, pixel[2] -60])
        image1 = cv2.inRange(hsv, rgbl, rgbh)
        image2=cv2.bitwise_and(image,image,mask=image1)
        cv2.imshow("window1", image2)

while(True):
    global rgbl,rgbh,image,image_h
    ret, image = frame.read(0)
    cv2.imshow("window", image)
    cv2.setMouseCallback('window', mouse_click)
    if(para==1):
        cv2.imshow("window1", cv2.medianBlur(image, 11))
    elif(para==2):
        cv2.imshow("window1", cv2.GaussianBlur(image, (5, 5), 0))

    elif(para==3):
         gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
         cv2.imshow("window1",gray)
    elif(para==4):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        image1 = cv2.inRange(hsv, rgbl, rgbh)
        image2 = cv2.bitwise_and(image, image, mask=image1)
        cv2.imshow("window1", image2)

    elif(para==5):
        b, g, r = cv2.split(image)
        image = cv2.merge((r, g, b))
        cv2.imshow("window1", image)
    elif(para==6):
        b, g, r = cv2.split(image)
        image = cv2.merge((b, g, r))
        cv2.imshow("window1", image)
    elif(para==0):
        cv2.imshow("window1", cv2.bilateralFilter(image, 31, 350, 350))
    k = cv2.waitKey(1)
    if k==ord('s'):
        para=5
        print("mixed")
    elif k==ord('n'):
        para=0
        print("boxfilter")
    elif k == ord(' '):
        break
frame.release()

# close all the opened windows.
cv2.destroyAllWindows()