# The current picture of car plate is not enough to train the model
# We use this file to create 4 image but cutting the upper and left side of the picture (by 10%)
# so each picture we can make at most 4 pictures
# we also ensure if the picture after cutting is cut the car plate, then we ignore it

from PIL import Image
import glob

path = 'Haar-Training_carPlate/training/positive/'
fp = open(path + 'info.txt', 'r')
lines = fp.readlines()  
count =  len(glob.glob("carPlate/*.bmp")) 

# just ensure if the picture is already created (no duplicate.)
if len(lines)>count:
    print("The new picture has been created!")

else:    
    rettext = ''
    print('Starting...')    
    for line in lines:
        data = line.split(' ')

        # image data
        img = Image.open(path + data[0])  
        x = int(data[2])  
        y = int(data[3])  
        w = int(data[4]) 
        h = int(data[5])  

        # reduce the width and heigh of the image
        reduceW = 30 
        reduceH = int(reduceW*0.75)  
        multi = float(300/(300-reduceW)) # the ratio of new picture and old picture
        neww = int(w*multi)  
        newh = int(h*multi)  

        # first pic: remove the upper left side of the picture
        if (x-reduceW)>5 and (y-reduceH)>5:  # only crop if have place
            count += 1  # use for naming
            newimg = img.crop((reduceW, reduceH, 300, 225))  # crop the pictue
            newimg = newimg.resize((300, 225), Image.ANTIALIAS)  # resize
            newimg.save(path + 'rawdata/bmpraw{:0>3d}.bmp'.format(count), 'bmp')  # save
            newx = int((x-reduceW)*multi-reduceW*(multi-1)/2)  
            newy = int((y-reduceH)*multi-reduceH*(multi-1)/2)            
            rettext = rettext+'rawdata/bmpraw{:0>3d}.bmp'.format(count)+' '+'1'+' '+str(newx)+' '+str(newy)+' '+str(neww)+' '+str(newh)+'\n'  # save new data to info.txt
        
        # second pic: remove upper right of the picture 
        if (x+w)<(300-reduceW-5) and y>(reduceW+5):
            count += 1
            newimg = img.crop((0, reduceH, (300-reduceW), 225))
            newimg = newimg.resize((300, 225), Image.ANTIALIAS)
            newimg.save(path + 'rawdata/bmpraw{:0>3d}.bmp'.format(count), 'bmp')
            newx = int(x*multi)
            newy = int((y-reduceH)*multi)
            rettext = rettext+'rawdata/bmpraw{:0>3d}.bmp'.format(count)+' '+'1'+' '+str(newx)+' '+str(newy)+' '+str(neww)+' '+str(newh)+'\n'
        
        # third pic: remove bottom left of the picture 
        if (x-reduceW)>5 and (y+h)<(225-reduceH-5):
            count += 1
            newimg = img.crop((reduceW, 0, 300, 225-reduceH))
            newimg = newimg.resize((300, 225), Image.ANTIALIAS)
            newimg.save(path + 'rawdata/bmpraw{:0>3d}.bmp'.format(count), 'bmp')
            newx = int((x-reduceW)*multi)
            newy = int(y*multi)
            rettext = rettext+'rawdata/bmpraw{:0>3d}.bmp'.format(count)+' '+'1'+' '+str(newx)+' '+str(newy)+' '+str(neww)+' '+str(newh)+'\n'
        
        # forth pic: remove bottom right of the picture
        if (x+w)<(300-reduceW-5) and (y+h)<(225-reduceH-5):
            count += 1
            newimg = img.crop((0, 0, (300-reduceW), 225-reduceH))
            newimg = newimg.resize((300, 225), Image.ANTIALIAS)
            newimg.save(path + 'rawdata/bmpraw{:0>3d}.bmp'.format(count), 'bmp')
            newx = int(x*multi)
            newy = int(y*multi)
            rettext = rettext+'rawdata/bmpraw{:0>3d}.bmp'.format(count)+' '+'1'+' '+str(newx)+' '+str(newy)+' '+str(neww)+' '+str(newh)+'\n'

    fp.close()
    
    fpmake = open(path + 'Info.txt', 'a')  
    fpmake.write(rettext)  # overwrite the previous data
    fpmake.close()
    print('Finished.')

    # At this stage, the data is set. Now change the data inside samples_creation.bat and haarTraining.bat by placing the number 
    # of datasets that provided.
    # the model is named haar_cascade.xml