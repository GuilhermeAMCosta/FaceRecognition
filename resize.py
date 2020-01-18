import cv2

img = cv2.imread('SFI-DK1-264-324.JPG', cv2.IMREAD_UNCHANGED)
img1 =img
print(img.shape[0], img.shape[1])
#shape[0] = y
#shape[1] = x

# resize image
resized = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LANCZOS4)

#rotate with resize
R = cv2.getRotationMatrix2D((img.shape[0]/2, img.shape[1]/2),30, 1.5)
output = cv2.warpAffine(img1, R,(img.shape[1], img.shape[0]))

cv2.imshow("Rotate", output)
print('Original Dimensions : ', img.shape)
print('Resized Dimensions : ', resized.shape)
print('Rotated Dimensions : ', output.shape)
cv2.imshow("Original image", img)
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()