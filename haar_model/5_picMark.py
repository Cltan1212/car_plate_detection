# After creating the bg.txt inside negative file, 
# I run the objectmarker.exe and the result is inside the info.txt

# Now, I want to mark the car plate in the picture to check if the 
# model can detect the car plate based on the info.txt

from PIL import Image, ImageDraw
import shutil, os
from time import sleep

def emptydir(dirname):
    if os.path.isdir(dirname):
        shutil.rmtree(dirname)
        sleep(2)  
    os.mkdir(dirname)

fp = open('Haar-Training_carPlate/training/positive/info.txt', 'r')
lines = fp.readlines()  
emptydir('picMark')
print('Draw rectangle on the picture...')

# rawdata/bmpraw001.bmp 1 44 117 167 44
# data = filename number_plates x y w h
for line in lines:
    data = line.split(' ')
    img = Image.open('Haar-Training_carPlate/training/positive/' + data[0])  #讀取檔案
    draw = ImageDraw.Draw(img) 
    n = data[1]  
    for i in range(int(n)):
        x = int(data[2+i*4])
        y = int(data[3+i*4])
        w = int(data[4+i*4])
        h = int(data[5+i*4])
        draw.rectangle((x, y, x+w, y+h), outline='red')
    filename = (data[0].split('/'))[-1]
    img.save('picMark/' + filename)  

fp.close()   
print('Finished.') 