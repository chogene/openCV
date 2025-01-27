import cv2 as cv
import numpy as np

image = cv.imread('/home/chogene/openCV/projects/marker_42.jpg')

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
aruco_dict = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_250)
param = cv.aruco.DetectorParameters()

detect = cv.aruco.ArucoDetector(aruco_dict, param)

corners, ids, rejected = detect.detectMarkers(gray)

print("Detected Markers: ", ids)

if ids is not None:
    cv.aruco.drawDetectedMarkers(images, corners, ids)
    cv.imshow("Detected Markers ", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
