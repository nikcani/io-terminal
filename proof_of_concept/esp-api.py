import sys
from time import sleep

from pi.lib.serialApi import SerialApi

serialApi = SerialApi()
serialApi.print_if_debug("python script started")

mode = "listen"
if len(sys.argv) > 1:
    mode = sys.argv[1]
serialApi.print_if_debug(mode)

if mode == "listen":
    try:
        while True:
            serialApi.listen_for_actions()
    except KeyboardInterrupt:
        serialApi.print_if_debug("interrupt")
elif mode == "lock":
    sleep(2)
    serialApi.lock_open()
    sleep(2)
    serialApi.lock_close()
elif mode == "debug":
    sleep(2)
    serialApi.display_print("HELLO WORLD!", "YES           NO")
    serialApi.display_clear()
    serialApi.display_color("255 000 000")
    serialApi.lock_open()
    serialApi.lock_close()
    serialApi.li_activate("4", "000 255 000")
    serialApi.li_clear()
    serialApi.write_package("test", "the", "hashtag#filter")

serialApi.print_if_debug("python script stopped")
del serialApi

# https://github.com/nikcani/smart-inventory/wiki/Technical-Docs#serial-protocol
