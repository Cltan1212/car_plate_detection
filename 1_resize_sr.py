# This program is used to resize the picture 
# to 300 x 225 since the initial pic is too big for training
import PIL
from PIL import Image
import glob
import shutil, os
from time import sleep

# empty and delete directory
def emptydir(dirname):
    if os.path.exists(dirname):
        shutil.rmtree(dirname)
        sleep(2)
    os.makedirs(dirname)

# resize image
def dirResize(src, dst):
    myfiles = glob.glob(src + '/*.jpg')  # find all the image that is .JPG
    emptydir(dst)
    print(src + ' directory:')
    print('start to convert the image to 300 x 225...')
    for i, f in enumerate(myfiles):
        img = Image.open(f)
        img_new = img.resize((300, 225), PIL.Image.ANTIALIAS)  
        outname = str("resizejpg") + str('{:0>3d}').format(i+1) + '.jpg'
        img_new.save(dst + '/' + outname)
    print('the conversion is done.\n')

# resize the directory
dirResize('carPlate_sr', 'carPlate')
dirResize('realPlate_sr', 'realPlate')

