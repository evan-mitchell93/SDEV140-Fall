from images import Image

image = Image("./imgs/wow.gif")
image.draw()
purple = (0,0,0)
y = image.getHeight()//2
for x in range(image.getWidth()):
    
    image.setPixel(x,y-1,purple)
image.draw()