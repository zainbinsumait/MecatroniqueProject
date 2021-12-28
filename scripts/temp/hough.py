import numpy as np
import cv2

def main(img):

	image = img
	
	# Loads an image
	src = cv.imread(cv.samples.findFile(image), cv.IMREAD_GRAYSCALE)
	dst = cv.Canny(src, 50, 200, None, 3)
	# Copy edges to the images that will display the results in BGR
	cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
	cdstP = np.copy(cdst)

	lines = cv.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)
	for i in range(0, len(lines)):
		rho = lines[i][0][0]
		theta = lines[i][0][1]
		a = math.cos(theta)
		b = math.sin(theta)
		x0 = a * rho
		y0 = b * rho
		pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
		pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
		cv.line(cdst, pt1, pt2, (0,0,255), 3, cv.LINE_AA)

	linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)

	if linesP is not None:
		for i in range(0, len(linesP)):
			l = linesP[i][0]
			cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA

	return cdstP
