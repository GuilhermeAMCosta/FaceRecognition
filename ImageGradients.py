import cv2
import numpy as np
from matplotlib import pyplot as plt

img_src = cv2.imread("SCMFI-005-01-01.JPG")
img = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(img, 100, 200)#CANNY
laplacian = cv2.Laplacian(img, cv2.CV_64F)#LAPLACE
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)#SOBELX
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)#SOBELY

plt.subplot(3, 3, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 3, 7), plt.hist(img.ravel(), 256, [0, 256])
plt.title('Histrogram'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 3, 2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 3, 3), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 3, 9), plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 3, 8), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
cv2.imshow("EDGE", edges)
plt.show()
plt.hist(img.ravel(), 256, [0, 256])
cv2.imshow("Grey Scale", img)
plt.show()

