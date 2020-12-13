import numpy as np
import cv2

a = np.ones([300,300,3],dtype='uint8')*255
wname = 'Shapes'
cv2.namedWindow(wname)

def shape(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(a,(x,y),(x+10,y+10),(0,0,0),-5)
    if event == cv2.EVENT_MOUSEMOVE:
        cv2.rectangle(a,(x,y),(x+10,y+10),(0,0,0),-5)
cv2.setMouseCallback(wname,shape)

while True:
    cv2.imshow(wname,a)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('c'):
        a[:,:] = 255 
cv2.destroyAllWindows()


# 1. Left Button DOwn
# 2. Mouse Move
# 3. Combine mouse move + Left button down

#cv2.rectangle(a,(50,50),(100,100),(255,0,0),-5)


# Hint for Combined
# 1. Take a variable for status checking of Left Mouse Event
# 2. Keep chaning the status according to the Left Mouse Event
