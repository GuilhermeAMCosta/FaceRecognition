import cv2
from matplotlib import pyplot as plt
import numpy as np

imgPaisagem = cv2.imread("SCMFI-005-01-01.JPG", cv2.IMREAD_GRAYSCALE)
imgTemplate = cv2.imread("SFI-WS1-178-224.JPG", cv2.IMREAD_GRAYSCALE)

#ORB
orb = cv2.ORB_create(nfeatures=20000)
keypoints_orb, descriptors = orb.detectAndCompute(imgPaisagem, None)

keypoints_orb_Template, descriptors_Template = orb.detectAndCompute(imgTemplate, None)

#Insere Pontos na Imagem
new_imgPaisagem = cv2.drawKeypoints(imgPaisagem, keypoints_orb, None)
new_imgTemplate = cv2.drawKeypoints(imgTemplate, keypoints_orb_Template, None)

#SHOW INFO
'''
plt.subplot(1, 2, 1), 'plt.imshow(new_imgPaisagem, cmap='gray')
plt.title('Landscape Image'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 2, 2), plt.imshow(new_imgTemplate, cmap='gray')
plt.title('Template Image'), plt.xticks([]), plt.yticks([])
plt.show()
'''
cv2.imshow("img", new_imgPaisagem)

cv2.waitKey(0)
cv2.destroyAllWindows()
