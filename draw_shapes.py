import cv2

image = cv2.imread('bgr.jpg', 1)
cv2.line(image, (0, 0), (400, 400), (255, 0, 0), 5)
cv2.rectangle(image, (0, 0), (100, 100), (0, 255, 0), 3)
cv2.circle(image, (200, 100), 40, (0, 0, 255), -1)
font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(image, 'hello', (104, 50), font, 2, (253., 155, 255), cv2.LINE_AA)
cv2.imshow("shapes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
