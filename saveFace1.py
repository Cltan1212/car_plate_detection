import cv2 

# get the detect classifier
casc_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(casc_path)

# get the image from the path
imagename = "images/person3.jpg" # change image if you wish
image = cv2.imread(imagename)
faces = faceCascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), flags = cv2.CASCADE_SCALE_IMAGE)
count = 1
for (x,y,w,h) in faces:
    # draw a rectangle around each face 
    cv2.rectangle(image, (x,y), (x+w,y+h), (128,255,0), 2) 
    filename = "images/face" + str(count)+ ".jpg"  # set the face image name
    image1 = image[y: y + h, x: x + w]       # get the face image
    image2 = cv2.resize(image1, (400, 400))  # resize
    cv2.imwrite(filename, image2)
    count += 1

# show the image
cv2.namedWindow("facedetect")
cv2.imshow("facedetect", image)
cv2.waitKey(0)  
cv2.destroyWindow("facedetect")