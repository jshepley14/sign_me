# Joe Shepley jshepley14@gmail.com
# 1/7/18
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt


TEXT_ROTATION = -14 #degrees
CHARS_PER_LINE = 14
LINES_PER_SIGN = 7
X_start = 345
Y_start = 180


# adds the rotated text to the image
def add_text(image, text, position):
	rows,cols, channel = image.shape
	blank_image = np.zeros(image.shape, np.uint8)
	texted_image = cv2.putText(img=np.copy(blank_image), text=text, org=position,fontFace=3, fontScale=0.6, color=(200,200,200), thickness=2)
	M = cv2.getRotationMatrix2D((cols/2,rows/2),TEXT_ROTATION,1)
	rotated_texted_image = cv2.warpAffine(texted_image,M,(cols,rows))
	image = image - rotated_texted_image
	return image


# organizes input text into chunks that fit on the sign
def organize_text(text):
	texts = []
	text_chunk = text.split()[0]
	for word in text.split()[1:]:
		old_text_chunk=text_chunk
		text_chunk+=" "
		text_chunk+=word
		if len(text_chunk) > CHARS_PER_LINE: #CHARS_PER_LINE chararacters per line
			texts.append(old_text_chunk)
			if len(texts) == LINES_PER_SIGN: # LINES_PER_SIGN lines on the sign
				return texts
			text_chunk = ''
			text_chunk+=word
	texts.append(text_chunk)
	return texts


# draws text on the image
def draw_text(word_chunks, image, x, y):
	for word_chunk in word_chunks:
		image = add_text(image, word_chunk, (x, y))
		y+=30
	return image



""" Main"""

input_text = sys.argv[1]
word_chunks = organize_text(input_text)
image = cv2.imread('trump-sign.jpg')
new_image = draw_text(word_chunks, image, X_start, Y_start)
cv2.imwrite('text_on_trump.png',new_image)
plt.imshow(new_image)
plt.show()