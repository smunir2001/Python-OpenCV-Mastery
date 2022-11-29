import cv2
import random

img = cv2.imread('../assets/MSFS2020_SS_1.png', -1)
# print(type(img), '\n')
# print(img.shape, '\n')
# print(img)
# print(img[0][45], '\n')

# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

tag = img[850:1050, 200:500]
img[100:300, 650:950] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()