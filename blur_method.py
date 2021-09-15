import cv2

import numpy as np

image=cv2.imread('IMG20210311081817.jpg',1)
metrix=np.ones((5,5),np.float32)/25
new_image=cv2.filter2D(image,-1,metrix)
cv2.imshow("image",image)
cv2.imshow("newimage",new_image)
cv2.waitKey()
cv2.destroyAllWindows()