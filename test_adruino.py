import serial
import time

arduino = serial.Serial(port='/dev/cu.usbmodem11201', baudrate=9600, timeout=1)
time.sleep(2)  # chờ Arduino khởi động

arduino.write(b'R')
print("Sent R")
time.sleep(3)
arduino.write(b'X')
print("Sent X")

arduino.close()