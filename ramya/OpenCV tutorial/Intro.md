# OpenCV (source: [tutorials](https://www.youtube.com/watch?v=kdLM6AOd2vc&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K) )
* Image processing library
* Works with C++,C,python
* Here,we are using python for OpenCV<br>
1. Digital images are stored in matrix [PPI =Pixel Per Inch].<br>
2. Digital images are 2-D arrays of pixels.<br>
### NumPy-->
* Highly optimized library for numeriacl operations.
* All OpenCV array structures are converted to-and-from NumPy arrays.
* More convineient indexing system rather than using for loops.
Installation Command:<br>
`pip install opencv-python`<br>
`import cv2 and cv2.__version__ //to check version of opencv:(in python shell)`

## Read,write and show images in opencv
```import cv2
img=cv2.imread("logo.png",1) #reads img
print(img) #prints img matrix
cv2.imshow("image",img) ##shows image
k= cv2.waitKey(0) #waits until we perform action
if k==27:
	cv2.destroyAllWindows(); #if esc key is typed
elif k==ord('s'):
	cv2.imwrite('logo_copy.jpg',img)  #if s button is typed 
	cv2.destroyAllWindows();
```
in imread() function,the second argument can take three values.
* 1==iMREAD_color(loads color image)
* 0==iMREAD_GRAYSCALE(loads image in grayscale mode)
* -1==iMREAD_UNCHANGED(loads image as such including alpha channel)

## Read,write and show videos in opencv
```import cv2
cap= cv2.VideoCapture(0) #captures video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out= cv2.VideoWriter("output.avi", fourcc, 20.0, (640,480)) #name of window,fourcc var,frames per sec,width n height
while(cap.isOpened()): #executes only when cap is opened
	ret,frame=cap.read() #ret takes boolean whether it was read or not,frame takes instance 
	if ret == True:
		print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #width of frame
		print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #height of frame
		out.write(frame)   #takes frame into out
		gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   #converts instance to gray
		cv2.imshow('frame',gray) #shows gray converted frame
		if cv2.waitKey(1) == ord('q'): #quits window if q is tapped
			break
cap.release()
out.release()
cv2.destroyAllWindows()
```

## functions to edit image
There are various functions like ```cv2.line(img, pt1, pt2, color(in bgr), thickness)``` , ```cv2.rectangle()```, ```cv2.arrowedLine()``` , ```cv2.circle()``` and ```cv2.putText(img,text,pt.,fontface,fontscale,thickness,linetype)```
```img = cv2.imread('logo.png')
font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,'opencv',(10,255), font, 4, (0,255,255), cv2.LINE_AA)
```

## Setting Camera Parameters-->
* it is done by ```cap.set(CAP_PROP_FRAME_WIDTH, 720)``` or ```cap.set(3, 720)``` to change width and for height similarly except the number associated with it is '4'.
* Even though we set width and height function for frame,OpenCV only allows some predefined resolutions like 640*480,1280*720 and 160*120
* Basically intrepeter sets the nearest allowed resolution.For example,if you would set frame height and width as 20,20.It would automatically set its resolution closest to thisi.e. 160*120.
* 160 * 120 is the shortest allwed resolution in opencv




