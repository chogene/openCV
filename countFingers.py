import numpy as np
import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0)
pTime = 0

# Detect hands
detectHands = mp.solutions.hands
hands = detectHands.Hands(static_image_mode=False,
                          max_num_hands=2,
                          min_detection_confidence=0.5,
                          min_tracking_confidence=0.5)

# Draw keypoints
drawPoints = mp.solutions.drawing_utils

# Thumb, Index, Middle, Ring, Pinky
finger_tips = [4, 8, 12, 16, 20]  

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    imgRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    handResult = hands.process(imgRGB)

    if handResult.multi_hand_landmarks:
        for handLms in handResult.multi_hand_landmarks:
            # Check which fingers are up
            fingers = []
            for tip_idx in finger_tips:
                h, w, c = frame.shape
                tip_y = handLms.landmark[tip_idx].y

                # Compare with joint below the tip
                base_y = handLms.landmark[tip_idx - 2].y  

                if tip_idx == 4:  # Special case for thumb
                    tip_x = handLms.landmark[tip_idx].x
                    base_x = handLms.landmark[tip_idx - 2].x
                    fingers.append(1 if tip_x > base_x else 0)
                else:
                    fingers.append(1 if tip_y < base_y else 0)

            # Count fingers up
            fingers_up = fingers.count(1)

            # Display the count
            cv.putText(frame, f'Fingers Up: {fingers_up}', (10, 150), 
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

            print("Number of fingers up: ", fingers_up)

            # Draw hand landmarks
            drawPoints.draw_landmarks(frame, handLms, detectHands.HAND_CONNECTIONS)

    # Display current FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(frame, f'FPS:{int(fps)}', (10, 70), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the resulting frame
    cv.imshow('Hand Detection', frame)

    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

