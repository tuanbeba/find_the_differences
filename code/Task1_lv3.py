import cv2
import numpy as np

# Đọc ảnh đầu vào
img = cv2.imread('image.png')
# Chuyển sang ảnh xám
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Phân ngưỡng ảnh xám
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# Tìm các contour trong ảnh phân ngưỡng
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Tìm contour có diện tích lớn nhất và nhỏ nhất
min_area = float('inf')
min_contour = None
for contour in contours:
    area = cv2.contourArea(contour)
    if area < min_area:
        min_area = area
        min_contour = contour
# Tìm hình chữ nhật bao quanh contour đó
x, y, w, h = cv2.boundingRect(min_contour)
# Lật ảnh theo chiều dọc
img_vert = cv2.flip(img[y:y+h, x:x+w], 1)
# Hiển thị ảnh sau khi đã cắt
# cv2.imshow('Vertical Flip', img_vert)
img[y:y+h, x:x+w] = img_vert
# Lưu lại ảnh
cv2.imwrite('image_3.png', img)
# Hiển thị ảnh kết quả và chờ người dùng nhấn phím bất kỳ để thoát
cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()