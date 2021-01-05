import serial

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM9'
ser.open()

while True:
   search = ser.readline()
   line = str(search)
   print(line)