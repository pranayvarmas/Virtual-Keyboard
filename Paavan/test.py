import requests
import cv2
import numpy as np
import urllib3
urllib3.disable_warnings()

url = "https://192.168.0.2:8080/shot.jpg"

import cv2
import numpy as np
import imutils

data = [[[0,160],[0,120],['a','A']],[[160,320],[0,120],['b','B']],[[320,480],[0,120],['c','C']],[[480,640],[0,120],['d','D']],[[0,160],[120,240],['e','E']],[[160,320],[120,240],['f','F']],[[320,480],[120,240],['g','G']],[[480,640],[120,240],['h','H']],[[0,160],[240,360],['i','I']],[[160,320],[240,360],['j','J']],[[320,480],[240,360],['k','K']],[[480,640],[240,360],['l','L']],[[0,160],[360,480],['m','M']],[[160,320],[360,480],['n','N']],[[320,480],[360,480],['o','O']]]

#to be changed accordingly with the orientation

shift = [[480,640],[360,480]]
string = ""
l = len(data)

def shift_finder(c1,c2):
	isshift = 0
	if (c1 > shift[0][0] and c1 <= shift[0][1] and c2 > shift[1][0] and c2 <= shift[1][1]) :
		isshift = 1
	return isshift

def letter_reader(c1,c2):
	for x in range(0,l,1):
		if (c1 > data[x][0][0] and c1 <= data[x][0][1] and c2 > data[x][1][0] and c2 <= data[x][1][1]) :
			return data[x][2][isshift]
	return ""

while True:
	output= np.ones((64, 1536, 1), dtype = "uint8")
	output.fill(255)	
	
	img_resp = requests.get(url,verify = False)
	img_arr = np.array(bytearray(img_resp.content),dtype=np.uint8)
	frame = cv2.imdecode(img_arr ,-1)	
	
	frame = cv2.resize(frame,(640,480))
	frame = cv2.flip(frame,-1)

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_red = np.array([0,120,70]) 
	upper_red = np.array([10,255,255])
	
	mask1 = cv2.inRange(hsv, lower_red, upper_red)
	
	lower_red = np.array([170,120,70])
	upper_red = np.array([180,255,255])

	mask2 = cv2.inRange(hsv,lower_red,upper_red)

	mask = mask1 + mask2

	cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	isshift = 0
	for c in cnts:
		area = cv2.contourArea(c)
		if area > 125 :
			cv2.drawContours(frame,[c],-1,(0,255,0),3)

			M = cv2.moments(c)

			cx = int(M["m10"]/M["m00"])
			cy = int(M["m01"]/M["m00"])

			cv2.circle(frame,(cx,cy),1,(255,255,255),-1)

			string = string + letter_reader(cx,cy)			
					
			print (string, end="\r")
			isshift = shift_finder(cx,cy)				

	cv2.imshow("frame",frame)
	cv2.putText(output, string, (20, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
	cv2.imshow('Output', output)	

	k = cv2.waitKey(100) # tobechanged for getting single letters (not a repetition) 
	if k==27:
		break


	
	
	#cv2.imshow("androidCam",frame)

	

cv2.destroyAllWindows()
