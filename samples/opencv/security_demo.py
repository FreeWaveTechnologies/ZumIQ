import cv2
import time
import imutils
import datetime
import numpy as np

SHOW_VIDEO = True
MIN_SAVE_SECONDS = 3.0
MIN_MOTION_FRAMES = 8
CAMERA_WARMUP_TIME = 2.5
DELTA_THRESH = 5
RESOLUTION = (640, 480)
MIN_AREA = 3500


ip_camera = "rtsp://192.168.111.50/live/ch00_0"

cap = cv2.VideoCapture(ip_camera)

if not cap.isOpened():
    print("Erroring in opening camera, check address " + ip_camera)
    exit(0)

print("[INFO] warming up...a pie...not really...camera")
time.sleep(CAMERA_WARMUP_TIME)
avg = None
last_save = datetime.datetime.now()

motion_counter = 0

while(True):
    ret, frame = cap.read()
    text = "Unoccupied"

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21,), 0)

    if avg is None:
        print("[INFO]: starting background model...cool stuff")
        avg = gray.copy().astype("float")
        continue

    cv2.accumulateWeighted(gray, avg, 0.5)
    frame_delta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))

    thresh = cv2.threshold(frame_delta, DELTA_THRESH, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contours = contours[0] if imutils.is_cv2() else contours[1]

    for contour in contours:
        if cv2.contourArea(contour) < MIN_AREA:
            continue

        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 10)
        text = "Occupied"

    cv2.putText(frame, "Status: {}".format(text),(10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

    if text == "Occupied" and (datetime.datetime.now() - last_save).seconds > MIN_SAVE_SECONDS:
        last_save = datetime.datetime.now()
        file_name = "objectFound " + last_save.strftime("%c") + ".jpeg"
        cv2.imwrite(file_name, frame)


    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
