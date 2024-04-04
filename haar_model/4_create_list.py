# I have download the HAAR model from here: https://github.com/sauhaardac/haar-training
# I also copied the file from carPlate to positive/rawdata and negative to negative directory
# here I want to write the bg file and put inside the negative file (bg.txt)

import glob,os

fp = open('Haar-Training_carPlate/training/negative/bg.txt', 'w')
files = glob.glob("Haar-Training_carPlate/training/negative/*.jpg")
print('Creating bg.txt...')
text=""
for file in files:
    basename=os.path.basename(file) 
    filename= "negative/" + basename # negative/negGray???.jpg                     
    text += filename + "\n"
    print(text)
    
fp.write(text) 
fp.close()   
print('Finished.')