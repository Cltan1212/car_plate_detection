# we also need to prepare a negative picture 
#(not including the car plate picture)
# here we resize the false picture and convert to grey color
# only minor changes compare to 1

import PIL
from PIL import Image
import glob
import shutil, os
from time import sleep

def emptydir(dirname):
    if os.path.isdir(dirname):
        shutil.rmtree(dirname)
        sleep(2)  
    os.mkdir(dirname)

myfiles = glob.glob("carNegative_sr/*.jpg")
emptydir('carNegative')
print('Start conversion')
for i, f in enumerate(myfiles):
    img = Image.open(f)
    img_new = img.resize((500, 375), PIL.Image.ANTIALIAS)
    img_new = img_new.convert('L')  # change to grey color
    outname = str("negGray") + str('{:0>3d}').format(i+1) + '.jpg'
    img_new.save('carNegative/'+ outname)

print('Finished.')