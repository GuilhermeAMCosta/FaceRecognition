#CORRECTLY GENERATE of X and Y
#Guilherme Augusto de Mattos Costa (21/05/2019)
import cv2
import numpy as np

from random import randint

img = cv2.imread("SCMFI-005-01-01.JPG")

#Dimensions of Landscape Image
height, width = img.shape[:2]
print("FEATURES OF IMAGE:\nHeight = ",height,"\nWidth = ",width,"\n")

print("FEATURES OF TEMPLATE:")
temp = cv2.imread("SFI-WS1-178-224.JPG")

#Dimensions of Template Image
height_temp, width_temp = temp.shape[:2]
print("Height = ", height_temp,"\nWidth = ", width_temp, '\n----------------------------------\nTo crop:\n', (width_temp/2),
      "< x <", (width - (width_temp / 2)), "\n", (height_temp / 2), "< y <", (height - (height_temp / 2)),"\n----------------------------------\n")

#Random Numbers
i=0
while i < 1:
    y = randint(0,height)
    x  = randint(0,width)
    if  x > (width_temp/2) and x < (width-(width_temp/2)) and y > (height_temp/2) and y < (height-(height_temp/2)):
        print('\nACEITO:\nx=', x, "y=", y,"(", i,")")
    else:
        print('\nREJEITADO:\nx=', x, "y=", y, "(", i, ")")
    i=i+1


#Cut LANDSCAPE image
crop_img = img[y:y+x, x:x+y]
cv2.imshow("CropImageLANDSCAPE", crop_img)
gray_crop_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

#Cut TEMPLATE image
crop_img1 = temp[y:y+x, x:x+y]
cv2.imshow("CropImageTEMPLATE", crop_img1)
gray_crop_img1 = cv2.cvtColor(crop_img1, cv2.COLOR_BGR2GRAY)

#Template Match
w, h = gray_crop_img1.shape[::-1]
result = cv2.matchTemplate(gray_crop_img, gray_crop_img1, cv2.TM_CCOEFF_NORMED)
loc = np.where(result >= 0.9)

for pt in zip(*loc[::-1]):
    cv2.rectangle(crop_img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 3)


cv2.imshow("Template Match", crop_img)

cv2.waitKey(0)
cv2.destroyAllWindows()


