from PIL import Image,ImageDraw
from PIL import ImageFont

# the image with lightgray with its background
img = Image.new("RGB",(300,400),"lightgray") 
drawimg=ImageDraw.Draw(img)

# draw ellipse - face
# ellipse((left, top, right, bottom), fill, outline)
drawimg.ellipse((50,50,250,250),width=3,outline="gold")

# draw pollygon - left and right eye
# polygon([(x1,y1), (x2,y2), ..., (xn, yn)][,fill, outline])
drawimg.polygon([(100,90),(120,130),(80,130)],fill="brown",outline="red") 
drawimg.polygon([(200,90),(220,130),(180,130)],fill="brown",outline="red")

# draw rectangle - nose
# rectangle((left, top, right, bottom)[,fill, outline])
drawimg.rectangle((140,140,160,180),fill="blue",outline="black")

# nose
drawimg.ellipse((100,200,200,220),fill="red") 

# text((x1, y1), text[, fill, font])
drawimg.text((130,280),"e-happy",fill="orange")             
img.show()
img.save("images/happyface.png")