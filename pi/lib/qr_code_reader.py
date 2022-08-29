import gc
from datetime import datetime

import cv2
import pyzbar.pyzbar as pyzbar


# width = 2592
# height = 1944
# camera.set(3,width)
# camera.set(4,height)

def decode_cam(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    barcodes = pyzbar.decode(gray)
    print('reading...', end='\r')
    for barcode in barcodes:
        barcode_data = barcode.data.decode('utf-8')
        barcode_type = barcode.type
        print("[" + str(datetime.now()) + "] Type:{} | Data: {}".format(barcode_type, barcode_data))
        x = barcode_data

        return x


def get_qr_code_data():
    print("get_qr_code_data")
    try:
        im = None
        camera = cv2.VideoCapture(0)
        while im is None:
            # Read current frame
            ret, frame = camera.read()
            im = decode_cam(frame)
            if im is not None:
                print(im)
                del camera
                del ret
                del frame
                gc.collect()
                return im
    except KeyboardInterrupt:
        print('interrupted!')
