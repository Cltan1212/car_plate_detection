# THIS PART IS FOR PRACTISE PURPOSE - Using 7238N2.JPG to practise cropping by contours
# the image will be saved inside cropMono
emptydir('cropMono')
image = cv2.imread('7238N2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # turn gray
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV) # turn to black white
contours1 = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours1[0]
letter_image_regions = [] # this array is used to store all the point that is detected

# put the contour points into the array
for contour in contours:
    (x,y,w,h) = cv2.boundingRect(contour)
    letter_image_regions.append((x,y,w,h))
letter_image_regoins = sorted(letter_image_regions, key=lambda x: x[0]) # use x to sort

# cropping each word from the contours
i = 1
for letter_bounding_box in letter_image_regions:
    x,y,w,h = letter_bounding_box
    print(x,y,w,h)
    
    # if the width >= 5 and the height is 29-39, we see this as a word, so we save
    if w >=5 and h>28 and h<40:
        letter_image = gray[y:y+h, x:x+w] # crop this from gray
        letter_image = cv2.resize(letter_image, (18, 38))
        cv2.imwrite('cropMono/{}.jpg'.format(i), letter_image)
        i += 1