import cv2

# read the file
img = cv2.imread('images/person1.jpg') 
print("img.shape=",img.shape) # (533, 800, 3)        
cv2.imshow("win1", img) 

# retrieve the face image
x,y,w,h=341,76,125,125
face = img[y: y + h, x: x + w]    

# change the B, G value of the face image
for row in range(y,y+h):     
    for col in range(x,x+w): 
        img[row,col][0]=0    # value of B
        img[row,col][1]=50   # value of G

cv2.imshow("win2", img) 
cv2.waitKey(0)  
cv2.destroyAllWindows()