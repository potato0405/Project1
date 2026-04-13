import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

last_print = time.time()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask_red = cv2.inRange(hsv, lower_red, upper_red)

    if (time.time() - last_print) >= 1:
        if cv2.countNonZero(mask_red) > 500:
            print("Red detected")
        else:
            print("No colour detected")
        last_print = time.time()
    
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()