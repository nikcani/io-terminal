from lib.serial_api import SerialApi

serialApi = SerialApi()
serialApi.print_if_debug("python script started")

try:
    while True:
        serialApi.listen_for_actions()
except KeyboardInterrupt:
    serialApi.print_if_debug("interrupt")

serialApi.print_if_debug("python script stopped")
del serialApi
