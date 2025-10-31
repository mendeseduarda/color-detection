import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
   _, frame = cap.read()
   hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   lower_color = np.array([110, 50, 50])
   upper_color = np.array([130, 255, 255])
   mask = cv2.inRange(hsv_frame, lower_color, upper_color)
   contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
   cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
   cv2.imshow("Color Detection", frame)
   if cv2.waitKey(1) & 0xFF == ord('x'):
       break

cap.release()
cv2.destroyAllWindows()