import serial


class SerialApi:
    def __init__(self, debug=True):
        self.debug = debug
        self.ser = serial.Serial()
        self.ser.port = '/dev/ttyUSB0'
        self.ser.baudrate = 9600
        self.ser.open()

    def __del__(self):
        self.ser.close()

    def print_if_debug(self, string):
        if self.debug:
            print(string)

    def listen_for_actions(self, left_pressed_callback, right_pressed_callback, callback_param):
        line = self.ser.readline().decode().strip()
        self.print_if_debug("received from serial interface: " + line)
        if line == "button_left_pressed":
            self.print_if_debug('button press detected: left')
            left_pressed_callback(callback_param)
        elif line == "button_right_pressed":
            self.print_if_debug('button press detected: right')
            right_pressed_callback(callback_param)

    def write_line(self, string):
        self.ser.write(str.encode(string))
        self.print_if_debug(str.encode(string))

    def write_package_line(self, string):
        string = str(string).replace("#", "=")
        string += "                "
        self.write_line(string[0:16])

    def write_package(self, first, second="", third=""):
        self.write_package_line(first)
        self.write_package_line(second)
        self.write_package_line(third)
        self.write_line("#")

    def display_print(self, first, second):
        self.write_package('display_print', first, second)

    def display_clear(self):
        self.write_package('display_clear')

    def display_color(self, color):
        self.write_package('display_color', color)

    def li_clear(self):
        self.write_package('li_clear')

    def li_activate(self, led, color):
        self.write_package('li_activate', led, color)

    def lock_open(self):
        self.write_package("lock_open")

    def lock_close(self):
        self.write_package("lock_close")
