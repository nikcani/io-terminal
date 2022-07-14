import sys
from time import sleep

import serial

DEBUG = True

mode = "listen"
if len(sys.argv) > 1:
    mode = sys.argv[1]
print(mode)

print("python script started")


def write_line(string):
    ser.write(str.encode(string))
    if DEBUG:
        print(str.encode(string))


def write_package_line(string):
    string = string.replace("#", "=")
    string += "                "
    write_line(string[0:16])


def write_package(first, second="", third=""):
    write_package_line(first)
    write_package_line(second)
    write_package_line(third)
    write_line("#")


ser = serial.Serial()
ser.port = '/dev/tty.usbserial-0001'
ser.baudrate = 9600
ser.open()

if mode == "listen":
    try:
        while True:
            print(ser.readline().strip())
    except KeyboardInterrupt:
        print("interrupt")
elif mode == "led_turn_on":
    write_package("led_turn_on", "", "")
elif mode == "debug":
    sleep(2)
    write_package("display_print", "HELLO WORLD!", "YES           NO")
    write_package("display_clear")
    write_package("display_color", "255 000 000", "")
    write_package("lock_open", "255 000 000", "")
    write_package("lock_close", "255 000 000", "")
    write_package("li_clear")
    write_package("li_activate", "4", "000 255 000")
    write_package("test", "the", "hashtag#filter")

ser.close()
print("python script stopped")

# https://github.com/nikcani/smart-inventory/wiki/Technical-Docs#serial-protocol
