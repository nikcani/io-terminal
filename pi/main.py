from time import sleep

from lib.serialApi import SerialApi

print("main started")

serialApi = SerialApi()

sleep(2)
print("1")
serialApi.display_print("HELLO WORLD!", "YES           NO")
print("2")
sleep(2)
serialApi.display_clear()
sleep(2)
serialApi.display_color("255 000 000")
sleep(2)
serialApi.li_activate(4, "000 255 000")
sleep(2)
serialApi.li_clear()
sleep(2)
serialApi.lock_open()
sleep(2)
serialApi.lock_close()
sleep(2)
serialApi.display_print("test the", "hashtag#filter")

del serialApi
