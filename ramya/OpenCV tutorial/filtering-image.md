## Filtering image using hsv-->
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
