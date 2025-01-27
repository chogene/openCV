import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

aruco_dict = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_250)

marker_id = 42
marker_size = 200
marker_image = cv.aruco.generateImageMarker(aruco_dict, marker_id, marker_size)

cv.imwrite("marker_42.jpg", marker_image)
plt.imshow(marker_image, cmap = 'gray', interpolation = 'nearest')
plt.axis("Off")
plt.title(f'ArUco Marker {marker_id}')
plt.show()
