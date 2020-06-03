# Trackers:-
* Trackers are the one you use to effect the image window with.
* To create a Tracker-->
   * ```cv2.createTrackbar('B','img',0,255,nothing)```(here,'B' is the name of Tracker,'img'-name of window,0-lowest number,255-highest          number,nothing-event)
* To get tracker's position-->
  * creating a variable and assigning it using cv2 function
  * example:- ```b=cv2.getTrackbarPos("B","img")```
  * If we want to apply the channels to the image using tracker,we can assign as ```img[:]=[b,g,r]``` with g and r variables assigned by       getTrackbarPos() 
