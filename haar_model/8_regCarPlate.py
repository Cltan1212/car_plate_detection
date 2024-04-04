# this file use haar_carplate.xml to detect the car plate
# only detect the first file in the real plate file
import cv2
import glob

files = glob.glob("realPlate/*.jpg")
img = cv2.imread(files[0])  
# img = cv2.imread('realPlate/resizejpg001.jpg')  
detector = cv2.CascadeClassifier('haar_carplate.xml')  # use the model
signs = detector.detectMultiScale(img, minSize=(76, 20), scaleFactor=1.1, minNeighbors=4)  # detect

# means if detect the car plate
if len(signs) > 0 :  
    for (x, y, w, h) in signs:  # draw the car plate
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        print(signs)
else:
    print('No car plate.')

cv2.imshow('Frame', img)  
cv2.waitKey(0)
cv2.destroyAllWindows()