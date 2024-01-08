import cv2
import numpy as np

picture = np.zeros(shape=(300, 300, 3), dtype="uint8")

cv2.line(picture, (0,0), (100, 100), (20, 60, 255), 3)
cv2.line(picture, (200,200), (300, 300), (20, 60, 255), 3)

cv2.circle(picture, center=(150, 150), radius=15, color=(0, 255, 0), thickness=4)

cv2.putText(picture, "HELLO WORLD !", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 0, 0), thickness=3)

cv2.imshow("Line", picture)

cv2.waitKey(0)
cv2.destroyAllWindows()

