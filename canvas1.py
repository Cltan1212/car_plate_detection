import cv2
import numpy as np

# create red canvas
canvas = np.ones((200, 250, 3), dtype="uint8") # height, weight
print(canvas.shape)
canvas[:] = (125, 40, 255) # color
cv2.imshow('canvas', canvas)

# create black background
bg = np.zeros((200, 250,1), np.uint8) 
print(bg.shape) #(200, 250, 1)
bg.fill(255)    

# fill the color from white to black
for j in range(200): 
    for i in range(250):
      bg[j][i].fill(255-i)

cv2.imshow("bg", bg) 

cv2.waitKey(0)
cv2.destroyAllWindows()