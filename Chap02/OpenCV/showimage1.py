# How to show the image by using OpenCV

import cv2

# create and destroy new window
cv2.namedWindow("ShowImage1")
cv2.namedWindow("ShowImage2")

image1 = cv2.imread("images/1.JPG") # color
image2 = cv2.imread("images/2.JPG", 0) # no color

cv2.imshow("ShowImage1", image1)
cv2.imshow("ShowImage2", image2)

cv2.waitKey(0)
cv2.destroyAllWindows()