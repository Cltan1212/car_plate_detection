import cv2

# show the coordinate of the image
def show(image): 
    for y in range(8,14):     
        for x in range(6,10): 
            print(image[y,x],end=" ")
        print()
    print()

# read the file
img = cv2.imread('images/face.jpg')  

# change to grey color
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
print("gray.shape=",gray.shape)
show(gray)

# change to black white color
_,thresh = cv2.threshold(gray, 187, 255, cv2.THRESH_BINARY) 
print("thresh.shape=",thresh.shape) 
show(thresh)

# grey color using previous method
gray2 = cv2.imread("images/face.jpg", 0) 
print("gray2.shape=",gray.shape) 
show(gray2)

# change to black white from gray2
# if > 100 change to 0
_,thresh2 = cv2.threshold(gray2, 187, 200, cv2.THRESH_BINARY_INV)
print("thresh2.shape=",thresh.shape) 
show(thresh2)