import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while True:
    ret, image = camera.read()

    cv2.rectangle(image, (100, 100), (200, 200), color=(25, 36, 98), thickness=2)

    cv2.line(image, (0, 0), (100, 100), color=(0, 255, 0), thickness=1)

    cv2.circle(image, (150, 150), radius=50, color=(0, 0, 130), thickness=2)

    cv2.putText( image, "Text Putting", (220, 220), cv2.FONT_HERSHEY_DUPLEX,1, color=(200, 0, 0))

    cv2.imshow("OzEngineer", image)

    if cv2.waitKey(25) % 0xFF == "q":
        break

camera.release()

cv2.destroyAllWindows()
