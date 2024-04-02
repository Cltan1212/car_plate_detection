import cv2

cv2.namedWindow("ShowImage")

image = cv2.imread("images/1.JPG", 0)

cv2.imshow("ShowImage", image)
cv2.imwrite("images/1copy1.png", image)
cv2.imwrite("images/1copy2.png", image, [int(cv2.IMWRITE_JPEG_QUALITY), 50])

cv2.waitKey(0)
cv2.destroyAllWindows()