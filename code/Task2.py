import cv2

# Đọc 2 ảnh đầu vào
img1 = cv2.imread('image.png')
img2 = cv2.imread('image_3.png')
# Trừ hai ảnh cho nhau
diff = cv2.absdiff(img1, img2)
# Chuyển đổi ảnh sang ảnh xám
gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
# Tăng độ tương phản
equalized = cv2.equalizeHist(gray)
# Ngưỡng ảnh để tách vật thể khỏi nền
ret, thresh = cv2.threshold(equalized, 0, 255, cv2.THRESH_BINARY)
# Phân vùng ảnh để tìm các vật thể
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# tìm khung bé nhất bao quanh tất cả các contours
x, y, w, h = cv2.boundingRect(contours[0])
for contour in contours:
    contour_x, contour_y, contour_w, contour_h = cv2.boundingRect(contour)
    x = min(x, contour_x)
    y = min(y, contour_y)
for contour in contours:
    contour_x, contour_y, contour_w, contour_h = cv2.boundingRect(contour)
    w = max(w, contour_x + contour_w - x)
    h = max(h, contour_y + contour_h - y)
# vẽ khung bé nhất
cv2.rectangle(img1, (x, y), (x+w, y+h), (0, 0, 0), 2)
cv2.rectangle(img2, (x, y), (x+w, y+h), (0, 0, 0), 2)
# Resize 2 ảnh cùng kích thướccv2.imshow('diff',diff)
img1 = cv2.resize(img1, (int(img1.shape[1]/2), int(img1.shape[0]/2)))
img2 = cv2.resize(img2, (int(img2.shape[1]/2), int(img2.shape[0]/2)))
# Ghép 2 ảnh theo chiều ngang
result = cv2.hconcat([img1, img2])
# Hiển thị ảnh ghép và chờ người dùng nhấn phím bất kỳ để thoát
cv2.imshow('Tim diem khac nhau',result)
cv2.waitKey(0)
cv2.destroyAllWindows()