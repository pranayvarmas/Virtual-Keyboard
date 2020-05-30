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

## Text on Videos-->
```import cv2
import datetime
cap = cv2.VideoCapture(0)
cap.set(3,1208)
cap.set(4, 720)
while(cap.isOpened):
    ret, frame = cap.read()
    if ret:
        details = "width: " + str(cap.get(3)) + " height: "+str(cap.get(4))
        date = str(datetime.datetime.now())
        font= cv2.FONT_HERSHEY_SIMPLEX
        frame = cv2.putText(frame, date, (10,30), font, 1, (0, 255, 255), 5, cv2.LINE_AA)
        cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break;
cap.release()
cv2.destroyAllWindows()
```
* we add text details or date that is concatenated string with a font,size,color
* it is done by ```frame=cv2.putText()``` ,providing proper arguments
* date and time can be shown by importing datetime module
* this is just a practice problem of concepts learnt earlier
* Syntax: ```cv2.putText(image, text, org, font, fontScale, color, thickness, lineType, bottomLeftOrigin)```<br>
Parameters:
	* image: It is the image on which text is to be drawn.
	* text: Text string to be drawn.
	* org: It is the coordinates of the bottom-left corner of the text string in the image. The coordinates are represented as 		  tuples of two values i.e. (X coordinate value, Y coordinate value).
	* font: It denotes the font type. Some of font types are FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN, , etc.
	* fontScale: Font scale factor that is multiplied by the font-specific base size.
	* color: It is the color of text string to be drawn. For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.
	* thickness: It is the thickness of the line in px.
	* lineType: This is an optional parameter.It gives the type of the line to be used.
	* bottomLeftOrigin: This is an optional parameter. When it is true, the image data origin is at the bottom-left corner. 		  Otherwise,it is at the top-left corner.
	
## Mouse  click events-->
* 'EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL', 'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP'(can be found by printing events in dir(cv2) like ```print(events=[i for i in dir(cv2) if "EVENTS" in i])```)
* for creating effect for an event,we define a function ```def click_event(event, x, y, flag, param):```.When we click the event button by calling ```cv2.setMouseCallback(img,click_event)```,x and y of the clicked position gets inserted to the function's arguments and we get the assigned work in function click_event.

## Drawing a black background using numpy-->
* ```numpy.zeros()``` is used to make a black background.zeros() function is used to insert zeros in a matrix we provide,here we provide ```numpy.zeros((512,512,3),numpy.uint8)```
* uint8 is used unsigned 8 bit integer(dtype argument in zeros()). And that is the range of pixel. We can't have pixel value more than 2^8 -1. Therefore, for images uint8 type is used. Whereas double is used to handle very big numbers
* to create white screen we use ```numpy.ones()*number```,where number is the brightness of white.If we give number 0,we get a black scree,if 230-greyish close to white.




