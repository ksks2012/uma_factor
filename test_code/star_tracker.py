import cv2
import numpy as np
# lower = np.array([240,210,80])  # 轉換成 NumPy 陣列，範圍稍微變小 ( 55->30, 70->40, 252->200 )
# upper = np.array([255,230,120]) # 轉換成 NumPy 陣列，範圍稍微加大 ( 70->90, 80->100, 252->255 )
lower = np.array([50,200,240])
upper = np.array([120,230,255])
img = cv2.imread('one.png')
output = cv2.inRange(img, lower, upper)             # 使用 inRange
# output = cv2.bitwise_and(img, img, mask = mask )  # 套用影像遮罩
cv2.imwrite('output_one.png', output)

img = cv2.imread('two.png')
output = cv2.inRange(img, lower, upper)             # 使用 inRange
# output = cv2.bitwise_and(img, img, mask = mask )  # 套用影像遮罩
cv2.imwrite('output_two.png', output)

# contours, hierarchy = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # 获取轮廓及层级关系
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
output = cv2.dilate(output, kernel)
output = cv2.erode(output, kernel)
cv2.imwrite('oxxostudio.png', output)

contours, hierarchy = cv2.findContours(output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# for contour in contours:
#     print(contour)

print(len(contours))

# if __name__ == '__main__':
#     pass