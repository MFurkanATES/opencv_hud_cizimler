import cv2

import numpy as np 
import time


img = cv2.imread('1.png',1)


#target = np.array([[213,60],[333,240],[93,240],[150,120]], np.int32)
#cv2.PolyLine(img, polys, is_closed, color, thickness=1, lineType=8, shift=0)
#cv2.polylines(img,[target],False,(255,20,50),thickness=1,lineType=8,shift=0)
#cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
merkez_x = 600
merkez_y = 400 

cv2.line(img,(merkez_x - 40,merkez_y),(merkez_x - 16,merkez_y),(150,255,50),1)
cv2.line(img,(merkez_x - 16,merkez_y),(merkez_x - 8,merkez_y + 8),(150,255,50),1)
cv2.line(img,(merkez_x - 8,merkez_y + 8),(merkez_x ,merkez_y ),(150,255,50),1)

cv2.line(img,(merkez_x ,merkez_y ),(merkez_x + 8,merkez_y + 8),(150,255,50),1)
cv2.line(img,(merkez_x + 8,merkez_y + 8),(merkez_x + 16,merkez_y),(150,255,50),1)
cv2.line(img,(merkez_x + 16,merkez_y),(merkez_x + 40,merkez_y ),(150,255,50),1)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
