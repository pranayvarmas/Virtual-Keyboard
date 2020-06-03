## Thresholding images
* Definition: Thresholding is a method of image segmentation, in general it is used to create binary images. Thresholding is of two types     namely, simple thresholding and adaptive thresholding.
### Simple Thresholding 
  * Is done by the function ```cv2.threshold(src,dst,threshold,maxvalue,type of threshold)```(dst is optional).
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
### Adaptive thresholding(of Improc class) 
* Is done by the function ```cv2.adaptiveThreshold(src,maxValue,type,blockSize,C)```
* In simple thresholding, the threshold value is global, i.e., it is same for all the pixels in the image. Adaptive thresholding is the    method where the threshold value is calculated for smaller regions and therefore, there will be different threshold values for          different regions.
* Examples-'ADAPTIVE_THRESH_GAUSSIAN_C', 'ADAPTIVE_THRESH_MEAN_C'
* ADAPTIVE_THRESH_MEAN_C − threshold value is the mean of neighborhood area.
* ADAPTIVE_THRESH_GAUSSIAN_C − threshold value is the weighted sum of neighborhood values where weights are a Gaussian window.
* Arguments-->
  * src − An object of the class Mat representing the source (input) image.
  * dst − An object of the class Mat representing the destination (output) image.
  * maxValue − A variable of double type representing the value that is to be given if pixel value is more than the threshold value.
  * adaptiveMethod − A variable of integer the type representing the adaptive method to be used. This will be either of the following       two values
  * thresholdType − A variable of integer type representing the type of threshold to be used.
  * blockSize − A variable of the integer type representing size of the pixelneighborhood used to calculate the threshold value.
  * C − A variable of double type representing the constant used in the both methods (subtracted from the mean or weighted mean)
