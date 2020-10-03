import cv2

# read image
global image,count,step,b,g,r
count,step=0,0

image = cv2.imread("wlp.jpg")
b,g,r=cv2.split(image)
# show image
cv2.imshow('window', image)
def avgBlur(img):
    global count
    count+=1
    return cv2.blur(img, (3,3))
def gaussBlur(img):
    global count
    count += 1
    return  cv2.GaussianBlur(img, (5,5), 0)
def medianBlur(img):
    global count
    count += 1
    return cv2.medianBlur(img, 11)
def bilfil(img):
    global count
    count += 1
    return cv2.bilateralFilter(img, 31, 350, 350)
def boxfil(img):
    global count
    count =0
    return cv2.boxFilter(img,-1,(5,5))
def filter1(img):
    global step,b
    step+=1
    return b
def filter2(img):
    global step,g
    step+=1
    return g
def filter3(img):
    global step
    step+=1
    return r
def filter4(img):
    global step
    step+=1
    return cv2.merge((b,g,r))
def filter5(img):
    global step
    step+=1
    return cv2.merge((b,r,g))
def filter6(img):
    global step
    step+=1
    return cv2.merge((g,b,r))
def filter7(img):
    global step
    step+=1
    return cv2.merge((g,r,b))
def filter8(img):
    global step
    step+=1
    return cv2.merge((r,b,g))
def filter9(img):
    global step
    step=0
    return cv2.merge((r,g,b))



# define the events for the
# mouse_click.
def mouse_click(event, x, y,flags, param):
    # to check if left mouse
    # button was clicked
    global image,count,step
    if event == cv2.EVENT_LBUTTONDOWN:
        print("left")
        print(count)
        if count==0:
            print("avg")
            cv2.imshow("window",avgBlur(image))

        elif count==1:
            print("gauss")
            cv2.imshow("window",gaussBlur(image))

        elif count==2:
            print("median")
            cv2.imshow("window",medianBlur(image))

        elif count==3:
            print("bila")
            cv2.imshow("window",bilfil(image))

        elif count==4:
            print("box")
            cv2.imshow("window",boxfil(image))

    if event == cv2.EVENT_RBUTTONDOWN:
        print("right")
        if step==0:
            print("bc")
            cv2.imshow("window", filter1(image))
        elif step==1:
            print("gc")
            cv2.imshow("window", filter2(image))
        elif step==2:
            print("rc")
            cv2.imshow("window", filter3(image))
        elif step==3:
            print("bgr")
            cv2.imshow("window", filter4(image))
        elif step==4:
            print("brg")
            cv2.imshow("window", filter5(image))
        elif step==5:
            print("gbr")
            cv2.imshow("window", filter6(image))
        elif step==6:
            print("grb")
            cv2.imshow("window", filter7(image))
        elif step==7:
            print("rgb")
            cv2.imshow("window", filter8(image))
        elif step==8:
            print("rbg")
            cv2.imshow("window", filter9(image))
    # if event== cv2.EVENT


cv2.setMouseCallback('window', mouse_click)

cv2.waitKey(0)

# close all the opened windows.
cv2.destroyAllWindows()