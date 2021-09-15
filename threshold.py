import cv2

image=cv2.imread('bgr.jpg',-1)
ret,tresh = cv2.threshold(image,60,255,cv2.THRESH_BINARY)
cv2.imshow("image",image)
cv2.imshow("tresh",tresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
