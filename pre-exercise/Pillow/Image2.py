from PIL import Image
img = Image.open("images/img01.jpg")
w,h=img.size #320 240

# image resize
img1=img.resize((w*2,h))
img1.save("images/resize01.jpg")