import cv2
import time
from houghDetection import *
#from hough import *

cap = cv2.VideoCapture(0)
print("press q to exit")

while(cap.isOpened()):
	#time.sleep(1)
	ret, frame = cap.read()

	ordre = main(frame)
	
	if cv2.waitKey(1) == 1048689: #if q is pressed
		break
	
	
###---------------------------------------------------------------###


###---------------------------------------------------------------###




#When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
