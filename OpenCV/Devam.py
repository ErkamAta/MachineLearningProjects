import cv2
import numpy as np

image = cv2.imread("agac.png")

cv2.imshow("Tree PNG", image)

image_2x = cv2.pyrUp(image)
cv2.imshow("2X Image Tree", image_2x)

little_image = cv2.pyrDown(image)
cv2.imshow("-2x Image", little_image)

print("Orjinal Resim Boyutu: ", image.shape)
print("2 Kat Büyütülmüş Resim: ", image_2x.shape)
print("2 Kat Küçük Resim: ", little_image.shape)

empty = np.zeros(shape=(300, 300, 3), dtype="uint8")
cv2.imshow("Zeros", empty)

cv2.waitKey(0)
cv2.destroyAllWindows()


print(np.zeros(shape=(300, 300, 3), dtype="uint8"))