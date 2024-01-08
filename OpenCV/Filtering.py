import cv2

image = cv2.imread("Tree.jpg")

mean_filter = cv2.blur(image, ksize=(3, 3))

median_filter = cv2.medianBlur(image, 3)

gauss_filter = cv2.GaussianBlur(image, (3, 3), 0)

cv2.imshow("Mean Filter (3x3)", mean_filter)
cv2.imshow("Tree", image)
cv2.imshow("Median Filter", median_filter)
cv2.imshow("Gauss Filter", gauss_filter)

cv2.waitKey(0)
cv2.destroyAllWindows()