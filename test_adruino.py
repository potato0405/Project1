import serial
import time

arduino = serial.Serial(port='/dev/cu.usbmodem11201', baudrate=9600, timeout=1)

while True:
    arduino.write(b'R')
    print('R')
    time.sleep(2)
    arduino.write(b'X')
    print('X')
    time.sleep(2)