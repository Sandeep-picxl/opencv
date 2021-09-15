import cv2

image = cv2.imread('bgr.jpg', 1)
print(image)
cv2.imshow('image', image)
cv2.waitKey(10000)
cv2.imwrite('bgr.jpg',image)
cv2.destroyAllWindows()
