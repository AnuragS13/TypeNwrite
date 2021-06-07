import os
from PIL import Image
import numpy as np


spacing = 50

def pasteLetter( opArray,blnk, letter, letterType):
    global spacing,xoffset
    top=0;
    bottom=0;
    if letterType==1:
        top = opArray[0]*spacing;
        bottom = opArray[2]*spacing;
    elif letterType==2:
        top = opArray[1]*spacing;
        bottom = opArray[2]*spacing;
    elif letterType==3:
        top = opArray[1]*spacing;
        bottom = opArray[3]*spacing;
    elif letterType==4:
        top = opArray[0]*spacing;
        bottom = opArray[3]*spacing;


    ht = bottom - top;
    xdim,ydim = letter.size
    letter = letter.resize((int((xdim/ydim)*ht),ht))
    xdim,ydim = letter.size
    for i in range(xdim):
        for j in range(ydim):
            pixel = letter.getpixel((i,j))
            if(pixel[0]<150):
                blnk.putpixel((i+xoffset,j+top),pixel)
    xoffset+=xdim



lst = os.listdir("/root/Documents/testing")

blnk = Image.open("/root/Documents/testing/Blank.jpg")

blnk=blnk.resize((2000,2828))
# lines = []
# for i in range(2828):
    # if(i%spacing==0):
        # lines.append(i)
dic={}

ls= os.listdir("/root/TypeNwrite/profiles/Priyansha_ki_writing/")
for item in ls:
    img = Image.open("/root/TypeNwrite/profiles/Priyansha_ki_writing/"+item)
    item.replace(".jpg","")
    item.replace(".png","")
    dic[item[0]]=(img,item[1])
    
s = """Hello my name is Lakhan
Mera naam hai lakhan
I dont like injection
fuck this shit"""

opArray = [0,1,2,3]

xoffset = 10

for ch in s:
    if(ch==' '):
        xoffset+=50
    elif(ch=='\n'):
        xoffset=10
        opArray= [item + 5 for item in opArray]
    else:
        pasteLetter(opArray,blnk,dic[ch][0],int(dic[ch][1]))

blnk.save("test_sample.jpg")
blnk.show();
