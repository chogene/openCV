import numpy as np
import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0)
pTime = 0
cTime = 0

# Detect hands
detectHands = mp.solutions.hands

# Number of hands to detect is 2 
# Minimum detection confidence is 0.5
# Minimum tracking confidence is set to 0.5
hands = detectHands.Hands(static_image_mode = False,
                          max_num_hands = 2,
                          min_detection_confidence = 0.5,
                          min_tracking_confidence = 0.5)

# Draw keypoints
drawPoints = mp.solutions.drawing_utils

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display current FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(frame, f'FPS:{int(fps)}', (20, 70), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    imgRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    handResult = hands.process(imgRGB)

    if handResult.multi_hand_landmarks:
        for handLms in handResult.multi_hand_landmakrs:
            for id, lm in enumerate(handLms, landmark):
                # height, width, circle
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                cv.circle(img, (cx, cy), 3, (255, 0, 255), cv.FILLED)

            drawPoints.draw_landmarks(img, handLms, detectHands.HAND_CONNECTIONS)

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
