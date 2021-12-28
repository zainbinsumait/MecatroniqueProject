import cv2
from houghDetection import *

cap = cv2.VideoCapture(0)
print("press q to exit")

while(cap.isOpened()):
	ret, frame = cap.read()

	frame = main(frame)
	
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) == 1048689: #if q is pressed
		break
	
	
###---------------------------------------------------------------###


###---------------------------------------------------------------###




#When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
