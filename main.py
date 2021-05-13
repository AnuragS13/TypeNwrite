import os
from PIL import Image



def textExtract(im):
    xdim,ydim = im.size
    out = Image.new("RGBA",im.size)
    yt=ydim
    yb=0
    xl=xdim
    xr=0
    for i in range(xdim):
        for j in range(ydim):
            pixel = im.getpixel((i,j))
            if(type(pixel)!=type(1) and len(pixel)>=3):
                if(not(pixel[0]>90 and pixel[1]>90 and pixel[2]>90)):
                    out.putpixel((i,j),(pixel[0],pixel[1],pixel[2],255))
                    yt=min(yt,j)
                    yb=max(yb,j)
                    xl=min(xl,i)
                    xr=max(xr,i)
                else:
                    out.putpixel((i,j),(0,0,0,0))
            else:
                if(pixel<80):
                    out.putpixel((i,j),(pixel,pixel,pixel,255))
                    yt=min(yt,j)
                    yb=max(yb,j)
                    xl=min(xl,i)
                    xr=max(xr,i)
                else:
                    out.putpixel((i,j),(0,0,0,0))
    # print((xl,yt,xr,yb))
    out=out.crop((xl,yt,xr,yb))
    xdim,ydim = out.size
    out=out.resize((int((xdim/ydim)*200),200))
    # out.save("small_a.png")
    return out
dic={}
lst = os.listdir("/root/Documents/testing")
for item in lst:
    if(item!="Blank.jpg"):
        im = Image.open("/root/Documents/testing/"+item,"r")
        xdim,ydim = im.size
        im=im.resize((int((xdim/ydim)*200),200))
        item = item.replace(".jpg","")
        dic[item]=textExtract(im)

imx = Image.open("/root/Documents/testing/Blank.jpg","r")

xdim,ydim = imx.size
imx=imx.resize((int((xdim/ydim)*2000),2000))
xdim,ydim = imx.size
res = Image.new("RGBA",imx.size)
for i in range(xdim):
    for j in range(ydim):
        res.putpixel((i,j),imx.getpixel((i,j)))

xoffset = 50
yoffset = 50

s = "ANURAG"

for ch in s:
    im=dic[ch]
    xcdim,ycdim = im.size
    for i in range(xcdim):
        for j in range(ycdim):
            pixel=im.getpixel((i,j))
            if(pixel[3]!=0):
                res.putpixel((i+xoffset,j+yoffset),pixel)
    xoffset+=xcdim+3

res.show()
