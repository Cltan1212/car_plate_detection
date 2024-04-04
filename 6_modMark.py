# The new type of car plate (in this dataset) is a bit different from the previous one.
# Since in the older car plate, the width of the car plate is 3 times of the height, but 
# in the new type of car plate, the width of the car plate is 3.8 times of the height, therefor
# we need to change the marking.

fp = open('Haar-Training_carPlate/training/positive/info.txt', 'r')
lines = fp.readlines()
rettext = ''
print("Starting to mark the car plate...")

for line in lines:
    data = line.split(' ')
    n = data[1]
    rettext += data[0] + ' ' + n +' '

    # read the data
    for i in range(int(n)):
        x = int(data[2+i*4])
        y = int(data[3+i*4])
        w = int(data[4+i*4])
        h = int(data[5+i*4])
        
        if (w/h) < 3.8:  
            newW = h * 3.8  # new width
            x -= int((newW - w) / 2)  # recalculate the x
            if x<=0:  x=0
            w = int(newW)
        rettext = rettext + str(int(x)) + ' ' + data[3+i*4] + ' ' + str(int(w)) + ' ' + data[5+i*4]

fp.close()

fp = open('Haar-Training_carPlate/training/positive/info.txt', 'w')
fp.write(rettext) 
fp.close()   
print('Finished.')

# note here only rewrite the info.txt, will need to run 5_picMark.py again