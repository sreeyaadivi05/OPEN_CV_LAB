import cv2
img =cv2.imread("image.png")
cv2.imshow("image.jpg", img)
cv2.imwrite("image.png", img)
cv2.imwrite("image.tiff", img)
cv2.imshow("image.png", img)
cv2.imshow("image.tiff", img)
cv2.waitKey(0)