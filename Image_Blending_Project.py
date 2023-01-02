import cv2
import numpy as np

#Read Two different image of same channel
img1 = cv2.imread("E:/Computer_Vision/Data/roi_opr.jpg")
img1 = cv2.resize(img1,(500,700))
img2 = cv2.imread("E:/Computer_Vision/Data/bro_thor.jpg")
img2 = cv2.resize(img2,(500,700))

def blend(x):
    pass

img = np.zeros((400,400,3),np.uint8)
cv2.namedWindow('win') #create track bar windows
cv2.createTrackbar('alpha','win',1,100,blend)
switch = '0:OFF \n 1:ON' #create switch for invoke the trackbars
cv2.createTrackbar(switch,'win',0,1,blend)

while(1):
    alpha = cv2.getTrackbarPos('alpha','win')
    s = cv2.getTrackbarPos(switch,'win')
    na = float(alpha/100)
    
    if s == 0:
        dst = img[:]
        
    else:
        dst = cv2.addWeighted(img1,1-na,img2,na,0)
        cv2.putText(dst,str(alpha),(20,50),cv2.FONT_ITALIC,2,(0,125,255),2)
    
    cv2.imshow('dst',dst)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
cv2.waitKey(0)
cv2.destroyAllWindows()


