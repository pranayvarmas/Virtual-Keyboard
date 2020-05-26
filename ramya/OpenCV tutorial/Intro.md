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

