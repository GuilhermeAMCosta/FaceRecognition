import cv2
import matplotlib.pyplot as plt
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread("SCMFI-017-03-01.JPG")
img = cv2.GaussianBlur(img,(5,5), cv2.BORDER_DEFAULT)
template = cv2.imread("SFI-WS1-178-224.JPG")
template = cv2.GaussianBlur(template, (1,1), cv2.BORDER_DEFAULT)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

#ORB
orb = cv2.ORB_create()
keypoints_orb, descriptors = orb.detectAndCompute(template_gray, None)

#HAARCASCADE
faces = face_cascade.detectMultiScale(img_gray, 1.3, 5)
faces_template = face_cascade.detectMultiScale(template_gray, 1.3, 5)

number_of_faces = 0
bestx = 0
besty = 0
number_of_matches = 0

print("Numero de Rostos Detectados:",len(faces))

for (x,y,w,h) in faces:
    #print("(",x,",", y, ")")
    #CROP
    crop_img = img_gray[y:y + h, x:x + w]

    #ORB
    keypoints_orb1, descriptors1 = orb.detectAndCompute(crop_img, None)
    #print("Len Desc:", len(descriptors1))
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descriptors, descriptors1)
    matching_result = cv2.drawMatches(crop_img, keypoints_orb, template_gray, keypoints_orb1, matches, None)
    print(len(matches))
    if number_of_matches < len(matches):
        number_of_matches = len(matches)
        bestx = x
        besty = y

    #SHOW RESULT
    cv2.imshow("Matching result", matching_result)
    cv2.waitKey(0)


    number_of_faces = number_of_faces + 1

#SHOW FACES IN LANDSCAPE IMAGE
cv2.rectangle(img,(bestx,besty),(bestx+w,besty+h),(255,0,0),3)
roi_gray = img_gray[besty:besty+h, bestx:bestx+w]
roi_color = img[besty:besty+h, bestx:bestx+w]


cv2.imshow('img',img)
print("Melhor Resultado:",number_of_matches, "\nCoordenadas:","(",bestx,",", besty, ")")
print("Número de Rostos Encontrados:", number_of_faces)
cv2.waitKey(0)
cv2.destroyAllWindows()




