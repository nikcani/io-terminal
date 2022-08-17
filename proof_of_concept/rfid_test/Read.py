
def myRead():
        #!/usr/bin/env python3
        import RPi.GPIO as GPIO
        from mfrc522 import SimpleMFRC522

        reader = SimpleMFRC522()
        try:
                print("Karte anlegen")
                id, text = reader.read()
                print(id)
                return text
        finally:
                GPIO.cleanup()

myRead()