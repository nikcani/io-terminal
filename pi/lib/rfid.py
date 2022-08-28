import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


def read_rfid_tag():
    reader = SimpleMFRC522()
    try:
        print("Karte anlegen")
        id, text = reader.read()
        print(id)
        print(text)
        return text
    finally:
        GPIO.cleanup()
