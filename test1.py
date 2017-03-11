import serial 
import time

ser = serial.Serial(
    port='/dev/cu.usbmodem1421',
    baudrate=9600,
    #parity=serial.PARITY_ODD,
    #stopbits=serial.STOPBITS_TWO,
    #bytesize=serial.SEVENBITS
)

print(ser.isOpen());
j=0
while j<100:
	i = ser.read();
	print(ord(i));
	j+=1
