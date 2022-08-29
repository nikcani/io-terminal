# Ein pair besteht aus einem/einer Schließfach/-nummer ((links) in dem Fall von 1 bis 6) und der ID des Users (mitte)
# und das asset_tag des Produktes, ist die ID leer dann ist das Schließfach auch leer man kann durch ein
# Hinzufügen eines dritten elements auch den inhalt des schließfaches einbetten erfordert aber kleine modifikationen
# im code
import time

from lib.qr_code_reader import get_qr_code_data
from lib.rfid import read_rfid_tag
from lib.serial_api import SerialApi
from lib.snipe_it_api import hardware_status_set_picked_up, hardware_status_set_ready_to_pickup, \
    hardware_checkin, hardware_status_set_ready_to_return, get_hardware_by_asset_id

serialApi = SerialApi()

boxAndCollectors = [
    (1, ('Karakan', '000069')),
    (2, ('', '')),
    (3, ('', '')),
    (4, ('', '')),
    (5, ('', '')),
    (6, ('', ''))
]
print(boxAndCollectors)


def get_user_id_from_rfid():
    username = read_rfid_tag().strip()
    print("======================================")
    print("gelesen wurde")
    print(username)
    print("======================================")
    return username


# suche nach dem NÄCHSTEN, FREIEN Platz
def is_there_space():
    for sf, (userRFID, assetID) in boxAndCollectors:
        if assetID == "":
            print("Nächstes freie Schließfach ist {}".format(sf))
            return sf
    print("Schließfächer alle voll")
    return False


# suche nach dem SF für den einen user
def where_user_item(user_id):
    for sf, (userRFID, assetID) in boxAndCollectors:
        if userRFID == user_id:
            print("Die Order des Users {} ist im Schließfach NR.: {}".format(user_id, sf))
            return sf, (userRFID, assetID)
    print("Order leider nicht vorhanden")
    return False


def admin_adds_order():
    user_rfid = get_user_id_from_rfid()
    if user_rfid == "admin":
        # admin, wenn er/sie etwas einlegen will
        asset_id = get_qr_code_data()
        username = get_hardware_by_asset_id(str(asset_id))
        sf = is_there_space()
        if not sf:
            print("Alle Schließfächer sind voll")
            return False
        open_lock()
        boxAndCollectors[sf - 1] = (sf, (username, asset_id))  # -1, weil ein array fängt bei 0 an, duh
        hardware_status_set_ready_to_pickup(int(asset_id))
        close_lock()
        print("==========Admin legt hinein===================")
        print(boxAndCollectors)
        print("==========Admin legte hinein===================")
    else:
        print("DU BIST KEIN ADMIN!!!!")


def admin_takes_order():
    user_rfid = get_user_id_from_rfid()
    if user_rfid == "admin":
        # button zum Einlegen hier
        # admin, wenn er/sie etwas entnehmen will
        for sf, (name, assetID) in boxAndCollectors:
            if name == "admin":
                boxAndCollectors[sf - 1] = (sf, ('', ''))
                hardware_checkin(int(assetID))
        close_lock()
        print("==========Admin nimmt Heraus===================")
        print(boxAndCollectors)
        print("==========Admin nahm Heraus===================")
    else:
        print("DU BIST KEIN ADMIN!!!!")


def user_brings_item_back():
    # User Kontext
    user_id = get_user_id_from_rfid()
    sf = is_there_space()
    if not sf:
        print("Alle Schließfächer sind voll")
        return False
    print("Im Schließfach NR.: {} ist Platz".format(sf))
    asset_id = get_qr_code_data()
    open_lock()
    boxAndCollectors[sf - 1] = (sf, ("admin", asset_id))  # -1, weil ein array fängt bei 0 an, duh
    hardware_status_set_ready_to_return(int(asset_id))
    close_lock()
    print("Die Bestellung des Users {} wurde in das Schließfach {} hinzugefügt".format(user_id, sf))
    return True


def user_takes_item():
    user_id = get_user_id_from_rfid()
    sf, (userRFID, assetID) = where_user_item(user_id)
    if not sf:
        print("Item nicht im Schließfach.")
        return False
    open_lock()
    boxAndCollectors[sf - 1] = (sf, ("", ''))  # Merke: Leere ID = Kein Item

    # id = asset id
    print("User {} hat item aus dem fach herausgenommen".format(user_id))
    hardware_status_set_picked_up(int(assetID))
    close_lock()
    return True


def open_lock():
    serialApi.lock_open()
    serialApi.li_activate(4, "000 255 000")


def close_lock():
    serialApi.li_activate(4, "255 000 000")
    serialApi.lock_close()
    time.sleep(1)
    serialApi.li_clear()


def put_in(user_id):
    if user_id == "admin":
        sf = is_there_space()
        if not sf:
            serialApi.display_color_red()
            serialApi.display_print("Alle Faecher", "sind voll.")
            time.sleep(5)
        else:
            serialApi.display_color_green()
            serialApi.display_print("Bitte Asset", "scannen.")
            asset_id = get_qr_code_data()
            username = get_hardware_by_asset_id(str(asset_id))
            open_lock()
            serialApi.display_print("Bitte einlegen!", "[DONE]  [CANCEL]")
            serialApi.listen_for_actions(is_put_in, close_lock, (sf, username, asset_id))
    else:
        serialApi.display_color_red()
        serialApi.display_print("Einlegen duerfen", "nur Admins.")


def take_out(user_id):
    if not where_user_item(user_id):
        serialApi.display_color_red()
        serialApi.display_print("Keine Entnahme", "moeglich.")
        time.sleep(5)
        serialApi.display_clear()
        serialApi.display_color_reset()
    else:
        pos, (user_id, asset_id) = where_user_item(user_id)
        boxAndCollectors[pos - 1] = (pos, ("", ''))  # Merke: Leere ID = Kein Item
        open_lock()
        serialApi.display_print("Bitte entnehmen!", "[DONE]  [CANCEL]")
        serialApi.listen_for_actions(took_out, close_lock, asset_id)


def took_out(asset_id):
    hardware_status_set_picked_up(int(asset_id))
    close_lock()


def is_put_in(tupel):
    sf, username, asset_id = tupel
    boxAndCollectors[sf - 1] = (sf, (username, asset_id))  # -1, weil ein array fängt bei 0 an, duh
    hardware_status_set_ready_to_pickup(int(asset_id))
    close_lock()


def main():
    serialApi.display_print("Bitte Karte vor ", "Sensor halten.  ")
    user_id = get_user_id_from_rfid()
    serialApi.display_print("Hallo {}".format(user_id), "[Rein]    [Raus]")
    serialApi.listen_for_actions(put_in, take_out, user_id)


while True:
    main()

# Tests
print(boxAndCollectors)
print("======================")
admin_adds_order()
print(boxAndCollectors)
print("======================")
print("USER TAKES ITEM")
user_takes_item()
print("======================")
print(boxAndCollectors)
print("======================")
print("USER BRINGS ITEM BACK")
user_brings_item_back()
print("======================")
print(boxAndCollectors)
print("======================")
print("ADMIN TAKES ORDER")
admin_takes_order()
print("======================")
print(boxAndCollectors)
