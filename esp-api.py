import serial
import sys

mode = "listen"
if len(sys.argv) > 1:
    mode = sys.argv[1]
print(mode)

print("python script started")


def write_package(first, second, third):
    ser.write(str.encode(first[0:15]))
    ser.write(str.encode(second[0:15]))
    ser.write(str.encode(third[0:15]))


ser = serial.Serial()
ser.port = '/dev/tty.usbserial-0001'
ser.baudrate = 9600
ser.open()

if mode == "listen":
    try:
        while True:
            # ser.write(b'1')
            print(ser.readline().strip())
    except KeyboardInterrupt:
        print("interrupt")
elif mode == "led_turn_on":
    write_package("Xled_turn_on", "", "")

ser.close()
print("python script stopped")

# https://github.com/nikcani/smart-inventory/issues/4#issuecomment-1123724680
