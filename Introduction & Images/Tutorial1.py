import cv2

img = cv2.imread('../assets/MSFS2020_SS_1.png', 0)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('NEW_MSFS2020_SS_1.png', img)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()