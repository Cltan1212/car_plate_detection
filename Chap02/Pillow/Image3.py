from PIL import Image
img = Image.open("images/img01.jpg")
imggray = img.convert('L') # convert to gray

imggray.save("images/gray01.jpg")