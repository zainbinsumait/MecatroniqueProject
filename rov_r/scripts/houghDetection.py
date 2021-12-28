import numpy as np
import cv2
import math

def main(img):

	#masked = cv2.
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray,(5,5),cv2.BORDER_DEFAULT)
	# apply image thresholding
	#ret, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY) #145
	img_edge = cv2.Canny(blur,220,255)

	img_dil = cv2.dilate(img_edge,np.ones((3,3)),iterations=1)

	# apply Hough Line Transformation
	lines = np.array([[[0, 0, 0, 0]],[[0, 0, 0, 0]]])
	lines = cv2.HoughLinesP(img_dil, 1, np.pi/180, 30, maxLineGap=200)
	#lines = cv2.HoughLinesP(img_dil, 1, np.pi/180, 30, maxLineGap=200)

	#print(lines)
	# Plot detected lines
	ordre  = 1
	temp = None
	if lines is None:
		print("alex")
	else:
		#cv2.line(img, (0, 0), (1300, 700), (255, 0, 0), 3)
		gaucheLines = 0
		droiteLines = 0
		for line in lines:
			x1, y1, x2, y2 = line[0]
			L = math.sqrt(abs(x2 - x1)**2 + abs(y2 - y1)**2)			
			alpha = math.acos(abs(x2-x1)/(0.00001+L)) *180/math.pi
			#print("longueur = " , round(L,4) , "angle = ",round(alpha,4))
			if (alpha > 30 and alpha < 55):
				#print(line)
				cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
				if ( x1 < 600 or x2 < 600):
					cv2.putText(img, 'gauche', (x1, y1) , cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 2, cv2.LINE_AA)
					gaucheLines = gaucheLines + 1
				else:				
					cv2.putText(img, 'droite', (x1, y1) , cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 2, cv2.LINE_AA)
					droiteLines = droiteLines + 1
		if gaucheLines < 4 and droiteLines > 4:
			ordre = 2
			print("va a gauche")
			print(gaucheLines)
		elif droiteLines < 4 and gaucheLines > 4:
			ordre = 3
			print(droiteLines)
			print("va a droite")
		else:
			ordre = 1
			print("tout droit! fonce!")	
	cv2.imshow('frame',img) 
 
	return ordre
