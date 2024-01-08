import cv2
import numpy as np

resim = cv2.imread("Tree2.jpg")
resim2 = cv2.imread("Tree.jpg")
tree_png = cv2.imread("agac.png")

cv2.imshow("Tree", resim)

resim2[50:120, 10:40] = [23, 10, 90]  # Piksele yeni renk atama
resim2[10:20, 10:20] = [0, 0, 0]

cv2.rectangle(resim2, (100, 700), (700, 100), [0, 0, 255], 2)

kesit = resim2[0:300, 0:300]
cv2.imshow("Kesit", kesit)

cv2.imshow("Tree2", resim2)

# cv2.imwrite("NewPicture", resim)


min_resim2 = resim2[0:700, 0:800]
min_resim = resim[0:700, 0:800]
agirlikli_toplama = cv2.addWeighted(min_resim2, 0.7, min_resim, 0.3, 0)
gray_image = cv2.cvtColor(tree_png, cv2.COLOR_BGR2GRAY)

toplam = cv2.add(min_resim, min_resim2)
cv2.imshow("Concat Image", toplam)
cv2.imshow("AgirlikToplama", agirlikli_toplama)
cv2.imshow("Gray Image", gray_image)

print(resim)
print(resim.size)
print(resim.dtype)

print(resim2[(30, 30)])  # Bu girdiğin konumdaki pikselin renk kodunu veriri.

yukseklik, genislik, kanalSayisi = tree_png.shape
print(f"Yüskesklik: {yukseklik}, Genişlik: {genislik}, Kanal Sayısı: {kanalSayisi}")

cv2.waitKey(0)
cv2.destroyAllWindows()
