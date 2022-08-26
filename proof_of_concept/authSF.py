# ein pair besteht aus einem/einer schliesßfach/-nummer ((links) in dem fall von 1-6) und der ID des Users (mitte) und das und das Assed_tag des Produktes, 
# ist die ID leer dann ist das schließfach auch leer
# man kann durch ein hinzufügen eines dritten elements auch den inhalt des schließfaches einbetten erfordert aber kleine modifikationen im code

import json
from telnetlib import STATUS
import rfid_test.Read as myRead
import request.get_Hardware as myReq
# import request.post_HardwareStatus as ChangeHwStatus
import request.post_hardwareCheckout as hwCheckOUT
import request.post_HardwareCheckin as hwCheckIN
import request.patch_changeHardwareStatus as changeHWStatusTo
import qrcode.qrCodeReader as qrCodeReader
import request.get_searchUserByAssetID as getSUBAssedID
import request.get_hardwareByStatus as getHWbyStatus

def getUserIDFormRFID():
    username = myRead.myRead().strip()  # RFID von der Karte
    print("======================================")
    print("gelesen wurde ")
    print(username)
    print("======================================")
    return username

boxAndCollectors =  [(1,( 'Karakan','000069')), (2, ('','')), (3,('','')), (4,('','')), (5,('','')), (6,('',''))]
print(boxAndCollectors)
temp = boxAndCollectors # testing || Orginal zustand der liste



# suche nach dem NÄCHSTEN FREIEN platz
def isThereSpace():
    for sf , (userRFID,assetID) in boxAndCollectors:
        if(assetID == ""):
            print("Nächstes freie Schließfach ist {}".format(sf))
            return sf
    print("Schließfächer alle voll")
    return False

# suche nach dem SF für den einen user
def whereUserItem(UserID):
    for sf , (userRFID,assetID) in boxAndCollectors:
        if(userRFID == UserID):
            print("Die Order des Users {} ist im Schließfach NR.: {}".format(UserID, sf))
            return sf , (userRFID,assetID)
    print("Order leider nicht vorhanden")
    return False


def adminAddsOrder():
    userRFID = getUserIDFormRFID()
    if userRFID == "admin":
        #admin wenn er/sie erwas reinlegen will
        assetID = qrCodeReader.getQRCodeData()
        username = getSUBAssedID.getHardwareByAssetID(str(assetID))
        sf = isThereSpace()
        if not (sf):
            print ("Alle Schließfächer sind voll")
            return False
        openSF()
        boxAndCollectors[sf-1] = (sf,(username,assetID)) #-1 weil ein array fängt bei 0 an, duh
        changeHWStatusTo.hardwareStatusToAbholbereit(int(assetID))
        closeSF()      
        print("==========Admin legt hinein===================")
        print(boxAndCollectors)
        print("==========Admin legte hinein===================")
    else:
        print("DU BIST KEIN ADMIN!!!!")

def adminTakesOrder():
    userRFID = getUserIDFormRFID()
    if userRFID == "admin":
        # button reinlegen Hier
        #admin wenn er/sie etwas rausnehmen will
        for sf,(name,assetID) in boxAndCollectors:
            if name == "admin":
                boxAndCollectors[sf-1] = (sf,('',''))
                hwCheckIN.hardwareCheckin(int(assetID))
        closeSF()
        print("==========Admin nimmt Heraus===================")
        print(boxAndCollectors)
        print("==========Admin nahm Heraus===================")
    else:
        print("DU BIST KEIN ADMIN!!!!")

def userBringsItemBack():
    #User Kontext
    UserID = getUserIDFormRFID()
    sf = isThereSpace()
    if not (sf):
        print ("Alle Schließfächer sind voll")
        return False
    print("Im Schließfach NR.: {} ist platz".format(sf))
    assetID = qrCodeReader.getQRCodeData()
    openSF()
    boxAndCollectors[sf-1] = (sf,("admin",assetID)) #-1 weil ein array fängt bei 0 an, duh
    changeHWStatusTo.hardwareStatusToRueckgabebereit(int(assetID))
    closeSF()
    print ("Die Bestellung des Users {} wurde in das Schließfach {} hinzugefügt".format(UserID,sf))
    return True


def userTakesItem():
    UserID = getUserIDFormRFID()
    sf, (userRFID, assetID ) = whereUserItem(UserID)
    if not (sf): 
        print("Item nicht im Schließfach.")
        return False
    openSF()
    boxAndCollectors[sf-1] = (sf,("",'')) # Mereke: Leere ID = Kein Item
    
    #id = asset id
    print("User {} hat item aus dem fach herausgenommen".format(UserID))
    changeHWStatusTo.hardwareStatusToAbgeholt(int(assetID))
    closeSF()
    return True


def getAssetIDFromQRScanner(): return "00002"

def openSF(): print("Schließfach öffnen")
def closeSF(): print("Schließfach schließen")


# Tests
print(temp)
print(boxAndCollectors)
print("======================")
adminAddsOrder()
print(temp)
print(boxAndCollectors)
print("======================")
print("USER TAKES ITEM")
userTakesItem()
print("======================")
print("USER BRINGS ITEM BACK")
userBringsItemBack()
print("======================")
print(boxAndCollectors)
print("======================")
print("ADMIN TAKES ORDER")
adminTakesOrder()
print("======================")
print(boxAndCollectors)
print(temp)

