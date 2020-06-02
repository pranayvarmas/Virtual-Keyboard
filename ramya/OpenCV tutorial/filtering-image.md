# Filtering image using hsv-->
* HSV -- Hue, Saturation, Value(https://www.researchgate.net/profile/Ravindran_G/publication/321126312/figure/fig1/AS:561582682722304@1510903153364/llustration-of-the-HSV-Color-Space-B-Color-Feature-Extraction-Color-feature-is-extracted.png)[see illustration]
    * Hue gives bandwidth of colors
    * Saturation gives depth of pigment
    * Value gives brightness of color
* We can filter images using either BGR or HSV.(better to use HSV)
* Here,we create trackbars of lower HSV values and higher HSV values so that we can pass that to array to mask the image to give masked resultant image.
    
```import numpy as np
import cv2 as cv
def nothing(x):
    pass
cv.namedWindow("Tracking")
cv.createTrackbar("LH","Tracking",0,255,nothing)
cv.createTrackbar("LS","Tracking",0,255,nothing)
cv.createTrackbar("LV","Tracking",0,255,nothing)
cv.createTrackbar("UH","Tracking",255,255,nothing)
cv.createTrackbar("US","Tracking",255 ,255,nothing)
cv.createTrackbar("UV","Tracking",255, 255,nothing)
while(True):
    frame=cv.imread('joker.png',1)
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lh= cv.getTrackbarPos("LH","Tracking")
    ls= cv.getTrackbarPos("LS","Tracking")
    lv= cv.getTrackbarPos("LV","Tracking")
    uh= cv.getTrackbarPos("UH","Tracking")
    us= cv.getTrackbarPos("US","Tracking")
    uv= cv.getTrackbarPos("UV","Tracking")
    l_b=np.array([lh,ls,lv])
    u_b=np.array([uh,us,uv])
    mask=cv.inRange(frame,l_b,u_b)
    res=cv.bitwise_and(frame, frame,mask=mask)
    cv.imshow("joker",frame)
    cv.imshow("mask",mask)
    cv.imshow("res",res)
    k=cv.waitKey(1)
    if k== 27:
        break
cv.destroyAllWindows()```
* The mask function takes the lower and upper bound hsv values to take only that colored parts in total image ,and we pass this mask to and operator so that we get the required colored regions in resultant image.
