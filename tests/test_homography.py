import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('washington.jpg.jpg')
rows,cols, channel = image.shape
blank_image = np.zeros(image.shape, np.uint8)
texted_image = cv2.putText(img=np.copy(blank_image), text="Ball is life.", org=(350,180),fontFace=3, fontScale=0.8, color=(200,200,200), thickness=2)
M = cv2.getRotationMatrix2D((cols/2,rows/2),-14,1)
rotated_texted_image = cv2.warpAffine(texted_image,M,(cols,rows))
image = image - rotated_texted_image
cv2.imwrite('text_on_washington.jpg.png',image)
plt.imshow(image)
plt.show()