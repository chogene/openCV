import numpy as np
import cv2 as cv
import time

cap = cv.VideoCapture(0)
pTime = 0
cTime = 0

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
     
    cv.putText(frame, f'FPS:{int(fps)}', (20, 70), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
