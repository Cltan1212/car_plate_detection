import cv2, numpy

cv2.namedWindow("plot")
image = cv2.imread("images/1.JPG")

# draw blue line
# line (image, start, end, color, width)
cv2.line(image, (50,50), (500, 200), (255,0,0), 2)

# draw rectangle
# rectangle(image, start, end, color, width)
cv2.rectangle(image, (100,200), (180, 300), (0, 255, 0), 3)

# draw circle
# circle(image, center, radius, color, width)   
cv2.circle(image, (300, 300), 40, (0, 255, 0), 2)

# draw polylines
# points = numpy.array([[first point], [second point], [third point],...])
# polylines(image, points, isClosed, color, width)
points = numpy.array([[20, 60], [300, 280], [150, 200]])
cv2.polylines(image, [points], True, (0, 0, 255), 2)

# put text
# putText(image, text, start, font, fontScale, color, width)
cv2.putText(image, "Hello OpenCV", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

cv2.imshow("plot", image)
cv2.waitKey(0)
cv2.destroyAllWindows()