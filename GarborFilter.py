import cv2
import numpy as np

g_kernel = cv2.getGaborKernel((21, 21), 8.0, np.pi/4, 10.0, 0.5, 0, ktype=cv2.CV_32F)

img_src = cv2.imread("SCMFI-005-01-01.JPG")
img = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)

filtered_img = cv2.filter2D(img, cv2.CV_8UC3, g_kernel)

cv2.imshow('image', img)
cv2.imshow('filtered image', filtered_img)

h, w = g_kernel.shape[:2]
g_kernel = cv2.resize(g_kernel, (3*w, 3*h), interpolation=cv2.INTER_CUBIC)
cv2.imshow('gabor kernel (resized)', g_kernel)

cv2.waitKey(0)
cv2.destroyAllWindows()