from lib.serial_api import SerialApi

serialApi = SerialApi()

serialApi.lock_open()

del serialApi
