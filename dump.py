import serial 
import time

ser = serial.Serial(
    port='/dev/cu.usbmodem1421',
    baudrate=9600
)

print(ser.isOpen());
j=0
while j<100:
	i = ser.read();
	if(i%5==1):
		print(i)
	if(i%5==4):
		print(i)
	j++
ser.close()
