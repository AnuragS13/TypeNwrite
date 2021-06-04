
import cv2
import numpy as np
 
# Picture path
img = cv2.imread('/root/Downloads/0_PNhBwYggh--M3Uja.png')
a = []
b = []
 
 
def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        a.append(x)
        b.append(y)
        cv2.circle(img, (x, y), 1, (0, 0, 255), thickness=-1)
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (0, 0, 0), thickness=1)
        cv2.imshow("image", img)
        if(len(a)>1):
            cv2.rectangle(img,(a[-2],b[-2]),(x,y),2)
            cv2.imshow("image", img)
            cropped = img[b[-2]:y , a[-2]:x]
            cv2.imshow("cropped",cropped);
        print(x,y)
 
 
cv2.namedWindow("image")
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
cv2.imshow("image", img)
cv2.waitKey(0)
print(a[0], b[0])
