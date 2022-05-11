import serial

ser = serial.Serial()
ser.port = '/dev/tty.usbserial-210'
ser.baudrate = 115200
ser.open()

try:
    while True:
        # ser.write(b'1')
        print(ser.readline())
except KeyboardInterrupt:
    print("finally")
    ser.close()
