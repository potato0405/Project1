import cv2
import numpy as np
import time
import serial

cap = cv2.VideoCapture(0)
arduino = serial.Serial(port='/dev/cu.usbmodem11201', baudrate=9600, timeout=1)

last_print = time.time()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    
    lower_green = np.array([40, 50, 50])
    upper_green = np.array([80, 255, 255])
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    if (time.time() - last_print) >= 1:
        if cv2.countNonZero(mask_red) > 500:
            print("Red detected")
            arduino.write(b'R')
        elif cv2.countNonZero(mask_green) > 500:
            print("Green detected")
            arduino.write(b'G')
        else:
            print("No colour detected")
            arduino.write(b'X')
        last_print = time.time()
    
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()