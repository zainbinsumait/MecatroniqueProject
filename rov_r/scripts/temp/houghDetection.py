import numpy as np
import cv2

def main(img):

	#masked = cv2.
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# apply image thresholding
	ret, thresh = cv2.threshold(gray, 130, 145, cv2.THRESH_BINARY)

	# apply Hough Line Transformation
	lines = cv2.HoughLinesP(thresh, 1, np.pi/180, 30, maxLineGap=200)
  
	# Plot detected lines
	for line in lines:
		x1, y1, x2, y2 = line[0]
		cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
 
	return img
