from PIL import Image
img = Image.open('images/img01.jpg')
img.show()
w,h = img.size # width and height
print(w,h)
filename = img.filename
print(filename)
