## Thresholding images
* Definition: Thresholding is a method of image segmentation, in general it is used to create binary images. Thresholding is of two types     namely, simple thresholding and adaptive thresholding.
* Simple Thresholding is done by the function ```cv2.threshold(src,dst,threshold,maxvalue,type of threshold)```(dst is optional).
  * src − An object of the class Mat representing the source (input) image.
  * dst − An object of the class Mat representing the destination (output) image.
  * thresh − A variable of double type representing the threshold value.
  * maxval − A variable of double type representing the value that is to be given if pixel value is more than the threshold value.
  * type − A variable of integer type representing the type of threshold to be used.
* Examples-'THRESH_BINARY', 'THRESH_BINARY_INV', 'THRESH_MASK', 'THRESH_OTSU', 'THRESH_TOZERO', 'THRESH_TOZERO_INV', 'THRESH_TRIANGLE',               'THRESH_TRUNC'
* We assign two variables to this threshold function .```_,th1=cv2.threshold(img,50,255,THRESH_BINARY)```
* For the [gradient image](https://pe-images.s3.amazonaws.com/basics/cc/gradients/essentials/photoshop-foreground-background-gradient.jpg),
  if we apply above type of threshold(binary),we get region having number above 50 will become white and region below 50 will become black.(Its inverse is ```cv2.THRESH_BINARY_INV```)
* For this [image](https://www.tutorialspoint.com/opencv/images/thresh_input.jpg)-->
  * ```THRESH_BINARY```--> [binary image](https://www.tutorialspoint.com/opencv/images/thresh_binary.jpg)
  * ```THRESH_BINARY_INV```--> [binary inverse image](https://www.tutorialspoint.com/opencv/images/thresh_binary_inv.jpg)
  * ```THRESH_TRUNC```-->[trunc image](https://www.tutorialspoint.com/opencv/images/thresh_trunc.jpg)
  * ```THRESH_TOZERO```-->[to_zero image](https://www.tutorialspoint.com/opencv/images/thresh_tozero.jpg)
  * ```THRESH_TOZERO_INV```-->[to_zero inverse image](https://www.tutorialspoint.com/opencv/images/thresh_tozero_inv.jpg)
