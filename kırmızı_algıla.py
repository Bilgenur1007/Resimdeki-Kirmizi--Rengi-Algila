import cv2
import numpy as np

while True:

    img = cv2.imread(r"C:\Users\bilge\PycharmProjects\pythonProject7\images (1).png")
    img_hsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    lower_red=np.array([0,70,50])
    upper_red=np.array([10, 255, 255])
    red_mask=cv2.inRange(img_hsv,lower_red,upper_red)
    cv2.imshow("img",img)
    cv2.imshow("reddmask",red_mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
