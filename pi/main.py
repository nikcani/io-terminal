# Ein pair besteht aus einem/einer Schließfach/-nummer ((links) in dem Fall von 1 bis 6) und der ID des Users (mitte)
# und das asset_tag des Produktes, ist die ID leer dann ist das Schließfach auch leer man kann durch ein
# Hinzufügen eines dritten elements auch den inhalt des schließfaches einbetten erfordert aber kleine modifikationen
# im code
import time

from lib.qr_code_reader import get_qr_code_data
from lib.rfid import read_rfid_tag
from lib.serial_api import SerialApi
from lib.snipe_it_api import hardware_status_set_picked_up, hardware_status_set_ready_to_pickup, \
    hardware_status_set_ready_to_return, get_assigned_user, hardware_checkin

serialApi = SerialApi()

boxAndCollectors = [
    (1, ('Karakan', '000069')),
    (2, ('Blocked', '000042')),
    (3, ('Blocked', '000073')),
    (4, ('', '')),
    (5, ('Blocked', '999998')),
    (6, ('Blocked', '999999'))
]
print(boxAndCollectors)


def get_user_id_from_rfid():
    return read_rfid_tag().strip()


def next_free_space():
    print(boxAndCollectors)
    for sf, (user_id, asset_id) in boxAndCollectors:
        if asset_id == "":
            print("Nächstes freie Schließfach ist {}".format(sf))
            return sf
    print("Schließfächer alle voll")
    return False


# suche nach dem SF für den einen user
def where_user_item(user_id):
    for sf, (user_id_stored, asset_id) in boxAndCollectors:
        if user_id_stored == user_id:
            print("Die Order des Users {} ist im Schließfach NR.: {}".format(user_id, sf))
            return sf, (user_id_stored, asset_id)
    print("Order leider nicht vorhanden")
    return False


def open_lock():
    serialApi.lock_open()
    serialApi.li_activate(4, "000 255 000")


def close_lock(tupel=()):
    print(tupel)
    serialApi.li_activate(4, "255 000 000")
    serialApi.lock_close()
    time.sleep(1)
    serialApi.li_clear()


def put_in(user_id):
    sf = next_free_space()
    if not sf:
        serialApi.display_color_red()
        serialApi.display_print("Alle Faecher", "sind voll.")
        time.sleep(5)
    else:
        serialApi.display_color_green()
        serialApi.display_print("Bitte Asset", "scannen.")
        asset_id = get_qr_code_data()
        open_lock()
        if user_id == "admin":
            assigned_user_id = get_assigned_user(str(asset_id))
            serialApi.display_print("Bitte einlegen!", "[DONE]  [CANCEL]")
            serialApi.listen_for_actions(is_put_in, close_lock, (sf, assigned_user_id, asset_id))
        else:
            serialApi.display_print("Bitte einlegen!", "[DONE]  [CANCEL]")
            serialApi.listen_for_actions(is_put_in, close_lock, (sf, "admin", asset_id))


def take_out(user_id):
    if not where_user_item(user_id):
        serialApi.display_color_red()
        serialApi.display_print("Keine Entnahme", "moeglich.")
        time.sleep(5)
        serialApi.display_clear()
        serialApi.display_color_reset()
    else:
        open_lock()
        pos, (user_id, asset_id) = where_user_item(user_id)
        serialApi.display_print("Bitte entnehmen!", "[DONE]  [CANCEL]")
        serialApi.listen_for_actions(took_out, close_lock, (pos, user_id, asset_id))


def took_out(tupel):
    close_lock()
    pos, user_id, asset_id = tupel
    boxAndCollectors[pos - 1] = (pos, ("", ""))
    if asset_id == "admin":
        hardware_checkin(asset_id)
    else:
        hardware_status_set_picked_up(int(asset_id))


def is_put_in(tupel):
    close_lock()
    sf, user_id, asset_id = tupel
    boxAndCollectors[sf - 1] = (sf, (user_id, asset_id))
    if user_id == "admin":
        hardware_status_set_ready_to_return(int(asset_id))
    else:
        hardware_status_set_ready_to_pickup(int(asset_id))


def main():
    close_lock()
    serialApi.display_clear()
    serialApi.display_color_reset()
    serialApi.display_print("Bitte Karte vor ", "Sensor halten.  ")
    user_id = get_user_id_from_rfid()
    serialApi.display_print("Hallo {}".format(user_id), "[Rein]    [Raus]")
    serialApi.listen_for_actions(put_in, take_out, user_id)


try:
    while True:
        main()
except KeyboardInterrupt:
    serialApi.print_if_debug("interrupt")
    del serialApi
