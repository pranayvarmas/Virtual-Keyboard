# Matplotlib in opencv-->
* Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.
* Matplotlib is a Python 2-D plotting library which produces pubication quality figures in a variety of hardcopy formats and ineractive       environments across platforms.
* additional features we have in matplotlib over static python.exe cv2.imshow() are x and y coordinates on hovering a point,zooming,placing   the image on window wherever we want,etc.
* ```from matplotlib import pyplot as plt
     import cv2
     img = cv2.imread("image.png",1)
     plt.imshow(img)
     plt.show()
     ```
* Here,we dont get a desired image .Because the plt gives image in RBG format whereas img in cv2 by BGR format.So,we first convert image by   ```img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)```
* See [matplotlib image](https://encrypted-tbn0.gstatic.com/images?                                                       q=tbn%3AANd9GcSmx3EvUDYdgJHbMk76d8AQsCBSijQI_BE2fbXU5nAgfappMPRE&usqp=CAU)
* If we dont want to see x and y marks on axes,we can use ```plt.xticks([]),plt.yticks([])```
* If we want to show set of images in one window-->
     * We list titles for all images,images array for storing all images
     * We use plt.subplot(rows,columns,index) to show images in window
     * ```img=cv2.imread('gradient.png',1)
          th_1=cv2.threshold(img,50,255,THRESH_BINARY)
          th_2=cv2.threshold(img,50,255,THRESH_BINARY_INV)
          th_3=cv2.threshold(img,50,255,THRESH_TRUNC)
          th_4=cv2.threshold(img,50,255,THRESH_TOZERO)
          th_5=cv2.threshold(img,50,255,THRESH_TOZERO_INV)
          titles = ['Original image','Binary','inverse binary','trunc','tozero','tozero inverse']
          images= ['img,th_1,th_2,th_3,th_4,th_5]
          for i in range(6):
               plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
               plt.title(titles[i])
               plt.xticks[()],plt.yticks[()]
          plt.show()
          ```
          
          
          
          
          
          
