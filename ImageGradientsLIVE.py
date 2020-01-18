import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    edges = cv2.Canny(frame, 100, 200)

    orb = cv2.ORB_create(nfeatures=15)
    keypoints_orb, descriptors = orb.detectAndCompute(edges, None)
    edges = cv2.drawKeypoints(edges, keypoints_orb, None)
    cv2.imshow('Canny', edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()