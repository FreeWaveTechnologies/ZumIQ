import cv2
import numpy as np

CAM_IP = "rtsp://192.168.111.50/live/ch01_0"

cap = cv2.VideoCapture(CAM_IP)

if not cap.isOpened():
    print("Erroring in opening camera, check address " + CAM_IP)
    exit(0)

while(True):
    ret, frame = cap.read() #Reading frame by frame
    cv2.putText(frame, 'Press q to quit',(10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
    cv2.imshow('FRAME', frame) #Opens a window to view the stream

    # Check to see if the q was pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

