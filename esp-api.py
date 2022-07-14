import sys
from time import sleep

import serial

DEBUG = True


def print_if_debug(string):
    if DEBUG:
        print(string)


def button_left_pressed():
    print_if_debug('button press detected: left')


def button_right_pressed():
    print_if_debug('button press detected: right')


def write_line(string):
    ser.write(str.encode(string))
    print_if_debug(str.encode(string))


def write_package_line(string):
    string = string.replace("#", "=")
    string += "                "
    write_line(string[0:16])


def write_package(first, second="", third=""):
    write_package_line(first)
    write_package_line(second)
    write_package_line(third)
    write_line("#")


def lock_open():
    write_package("lock_open")


def lock_close():
    write_package("lock_close")


print_if_debug("python script started")

mode = "listen"
if len(sys.argv) > 1:
    mode = sys.argv[1]
print_if_debug(mode)

ser = serial.Serial()
ser.port = '/dev/tty.usbserial-0001'
ser.baudrate = 9600
ser.open()

if mode == "listen":
    try:
        while True:
            line = ser.readline().decode().strip()
            print_if_debug("received from serial interface: " + line)
            if line == "button_left_pressed":
                button_left_pressed()
            elif line == "button_right_pressed":
                button_right_pressed()
    except KeyboardInterrupt:
        print_if_debug("interrupt")
elif mode == "lock":
    sleep(2)
    lock_open()
    sleep(2)
    lock_close()
elif mode == "debug":
    sleep(2)
    write_package("display_print", "HELLO WORLD!", "YES           NO")
    write_package("display_clear")
    write_package("display_color", "255 000 000", "")
    lock_open()
    write_package("lock_close")
    write_package("li_activate", "4", "000 255 000")
    write_package("li_clear")
    write_package("test", "the", "hashtag#filter")

ser.close()
print_if_debug("python script stopped")

# https://github.com/nikcani/smart-inventory/wiki/Technical-Docs#serial-protocol
