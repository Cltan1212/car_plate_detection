# after resizing, the bmp file is required for Haar model
from PIL import Image
import glob
import os

myfiles = glob.glob("carPlate/*.jpg")
print('start converting the picture to bmp format...')
for f in myfiles:
    namespilt = f.split("/")
    img = Image.open(f)
    outname = namespilt[1].replace('resizejpg', 'bmpraw') # replace the name
    outname = outname.replace('.jpg', '.bmp') 
    img.save('carPlate/'+ outname, 'bmp')     
    os.remove(f)
print('finished the conversion.')