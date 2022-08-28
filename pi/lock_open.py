from lib.serialApi import SerialApi

serialApi = SerialApi()

serialApi.lock_open()

del serialApi
