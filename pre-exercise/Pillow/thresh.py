import cv2
from PIL import Image
import numpy as np

# open pic with gray mode
gray = cv2.imread("images/img01.jpg", 0) 
# change gray to black and white
_,thresh = cv2.threshold(gray, 99, 255, cv2.THRESH_BINARY) 
cv2.imwrite("images/thresh1.jpg", thresh) # save the image

img = Image.open('images/img01.jpg')
w,h=img.size 
# convert to gray with pillow
img = img.convert('L')  
# convert to white and black
for i in range(w):      
    for j in range(h):  
        if img.getpixel((i,j)) <99:  
            img.putpixel((i,j),(0))  # set to black
        else:
            img.putpixel((i,j),(255)) # set to white
img.save("images/thresh2.jpg")       