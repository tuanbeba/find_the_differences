import cv2
import numpy as np
# Load ảnh
img = cv2.imread('image.png')
# Chuyển sang ảnh xám
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Tăng độ tương phản
equalized = cv2.equalizeHist(gray)
# Phân ngưỡng ảnh xám
ret, thresh = cv2.threshold(equalized, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# Tìm các contour trong ảnh phân ngưỡng
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Tìm contour có diện tích nhỏ nhất
min_area = float('inf')
min_contour = None
for contour in contours:
    area = cv2.contourArea(contour)
    if area < min_area:
        min_area = area
        min_contour = contour
# Tạo mask bằng cách vẽ contour lên ma trận mask
mask = np.zeros_like(gray)
cv2.drawContours(mask, [min_contour], 0, 255, -1)
img[mask > 0] = [232, 40, 227]
# Ghi ảnh ra file mới
cv2.imwrite('image_2.png', img)
# Hiển thị ảnh
cv2.imshow('image2', img)
cv2.waitKey(0)
cv2.destroyAllWindows()