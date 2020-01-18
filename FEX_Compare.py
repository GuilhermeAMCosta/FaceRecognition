import cv2
import numpy as np

img = cv2.imread("SCMFI-001-01-01.JPG", cv2.IMREAD_GRAYSCALE)
img_1 = cv2.imread("SCMFI-005-01-01.JPG", cv2.IMREAD_GRAYSCALE)

orb = cv2.ORB_create(nfeatures=1000)
keypoints_orb, descriptors = orb.detectAndCompute(img, None)
keypoints_orb1, descriptors1 = orb.detectAndCompute(img_1, None)


#Brute Force Matching compare the descripstors

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
matches = bf.match(descriptors, descriptors1)
print("Number of Matches:",len(matches))
print(keypoints_orb)
#print(descriptors)
#print(descriptors1)
#print(matches)
matching_result = cv2.drawMatches(img, keypoints_orb, img_1, keypoints_orb1, matches, None)


#cv2.imshow("Image", img)
cv2.imshow("Image 1", img_1)
cv2.imshow("Matching result", matching_result)
cv2.waitKey(0)
cv2.destroyAllWindows()