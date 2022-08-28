from lib.serialApi import SerialApi

serialApi = SerialApi()

serialApi.lock_close()

del serialApi
