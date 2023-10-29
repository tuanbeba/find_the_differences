import cv2
import numpy as np

# đọc ảnh
img = cv2.imread('image.png')
# chuyển đổi màu từ BGR sang HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# tạo mặt nạ vật thể bằng cách chỉ định phạm vi giá trị màu cần đổi
lower_color = np.array([97, 255, 232])  # giá trị màu thấp nhất
upper_color = np.array([101, 255, 232])  # giá trị màu cao nhất
mask = cv2.inRange(hsv, lower_color, upper_color)

# chuyển đổi màu trong vật thể sang màu Green
result = img.copy()
result[mask > 0] = [0, 255, 0]
# Ghi ảnh ra file mới
cv2.imwrite('image_1.png', result)
# hiển thị ảnh
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()