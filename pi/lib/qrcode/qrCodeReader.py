import cv2
import pyzbar.pyzbar as pyzbar
from datetime import datetime

#width = 2592
#height = 1944

camera = cv2.VideoCapture(0)
#camera.set(3,width)
#camera.set(4,height)

def decodeCam(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    barcodes = pyzbar.decode(gray)
    print('reading...', end='\r')
    for barcode in barcodes:
      barcodeData = barcode.data.decode('utf-8')
      barcodeType = barcode.type
      print("["+str(datetime.now())+"] Type:{} | Data: {}".format(barcodeType, barcodeData))
      return barcodeData

def getQRCodeData():  
  try:
    im = None
    while im is None:
      # Read current frame
      ret, frame = camera.read()
      im=decodeCam(frame)
      if im is not None:
        return im
  except KeyboardInterrupt:
    print('interrupted!')