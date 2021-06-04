from PIL import Image

im = Image.open("/root/Documents/testing/L.jpg","r")
im=im.crop((100,0,im.size[0],im.size[1]))
# im.show()
im.save("/root/Documents/testing/L.jpg")
