import cv2,glob
import numpy as np

# get the files that need to merge
files = glob.glob('cropMono/*.jpg') 
n=len(files) 

# the extra space to add to the edges
spaceX = 10  
spaceY = 8   
offset=1    # the space between number

# get the image info from the first image
img = cv2.imread(files[0])  
h,w=img.shape[0],img.shape[1]

# create white background
bg = np.zeros((h+2*spaceY, (w+offset)*n+2*spaceX, 1), np.uint8)
bg.fill(255)  

# add the picture to the bg canvas
for m,file in enumerate(files):
    gray = cv2.imread(file,0)  
    _,thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)  
    for row in range(h):  
        for col in range(w):
            bg[spaceY+row][spaceX+col+(w+offset)*m] = thresh[row][col] 

# save the image
cv2.imwrite('images/merge.jpg', bg) 
    
# show image
merge = cv2.imread("merge.jpg") 
cv2.imshow("merge",merge) 
cv2.waitKey(0)  
cv2.destroyAllWindows()