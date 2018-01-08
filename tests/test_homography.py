import cv2
import numpy as np
import matplotlib.pyplot as plt



refPt = []
cropping = False
global M

# handles manual cropping via clicking
def point_selection(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, cropping

    # check to see if the left mouse button was released
    if event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((x, y))
        cropping = False


# load the image, clone it, and setup the mouse callback function

image = cv2.imread('washington.jpg')
rows,cols, channel = image.shape
clone = image.copy()

"""
cv2.namedWindow("image")
cv2.setMouseCallback("image", point_selection)

# keep looping until the 'q' key is pressed
while True:
	# display the image and wait for a keypress
	cv2.imshow("image", image)
	key = cv2.waitKey(1) & 0xFF
 
	# if the 'r' key is pressed, reset the cropping region
	if key == ord("r"):
		image = clone.copy()
 
	# if the 'c' key is pressed, break from the loop
	elif key == ord("q"):
		break

print(refPt)
"""

def add_text(image, text, position):
	blank_image = np.zeros(image.shape, np.uint8)
	texted_image = cv2.putText(img=np.copy(blank_image), text=text, org=position, fontFace=3, fontScale=1, color=(200,200,200), thickness=2)
	
	rotated_texted_image = cv2.warpPerspective(texted_image,M,(cols, rows))
	image = image - rotated_texted_image
	return image


refPt = [(312, 153), (688, 41), (354, 452), (765, 413)]
pts1 = np.float32(refPt)
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)
val, M = cv2.invert(M)


image = add_text(image, "Ball is life.", (75, 90))
image = add_text(image, "Ball is life.", (75, 140))
image = add_text(image, "Ball is life.", (75, 220))
image = add_text(image, "Ball is life.", (75, 280))

cv2.imwrite('text_on_washington.jpg.png',image)
plt.imshow(image)
plt.show()