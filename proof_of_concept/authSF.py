# ein pair besteht aus einem/einer schliesßfach/-nummer ((links) in dem fall von 1-6) und der ID des Users (mitte) und das und das Assed_tag des Produktes, 
# ist die ID leer dann ist das schließfach auch leer
# man kann durch ein hinzufügen eines dritten elements auch den inhalt des schließfaches einbetten erfordert aber kleine modifikationen im code

import json
from telnetlib import STATUS
import Read as myRead
import request.get_Hardware as myReq
# import request.post_HardwareStatus as ChangeHwStatus
import request.post_hardwareCheckout as hwCheckOUT
import request.post_HardwareCheckin as hwCheckIN
import qrcode.qrCodeReader as qrCodeReader
import request.get_searchUserByAssetID as getSUBAssedID

def getUserIDFormRFID():
    username = myRead.myRead().strip()  # RFID von der Karte
    print("======================================")
    print("gelesen wurde ")
    print(username)
    print("======================================")
    return username

boxAndCollectors =  [(1,( '','')), (2, ('Karakan','000069')), (3,('','')), (4,('','')), (5,('','')), (6,('',''))]

temp = boxAndCollectors # testing || Orginal zustand der liste

userRFID = getUserIDFormRFID()

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

#
def addOrderNextFreeSfFor(UserID):
    if userRFID == "admin":
        #admin wenn er/sie etwas rausnehmen will
        # code fürs rausnehmen hier 
        #admin wenn er/sie erwas reinlegen will
        assetID = qrCodeReader.getQRCodeData()
        username = getSUBAssedID.getHardwareByAssetID(str(assetID))
        sf = isThereSpace()
        if not (sf):
            print ("Alle Schließfächer sind voll")
            return False
        openSF()
        boxAndCollectors[sf-1] = (sf,(username,assetID)) #-1 weil ein array fängt bei 0 an, duh
        closeSF()
        

        
    else:
        sf = isThereSpace()
        if not (sf):
            print ("Alle Schließfächer sind voll")
            return False
        #pseudo ID erwarte es vom QR Scanner
        assetID = qrCodeReader.getQRCodeData()
        openSF()
        boxAndCollectors[sf-1] = (sf,(UserID,assetID)) #-1 weil ein array fängt bei 0 an, duh
        
        hwCheckIN.hardwareCheckin(UserID,assetID)
        closeSF()
        print ("Die Bestellung des Users {} wurde in das Schließfach {} hinzugefügt".format(UserID,sf))
    return True


# def userTakesItem(UserID):
#     sf, (userRFID, assetID ) = whereUserItem(UserID)
#     if not (sf): 
#         print("Item nicht im Schließfach.")
#         return False
#     openSF()
#     boxAndCollectors[sf-1] = (sf,("",'')) # Mereke: Leere ID = Kein Item
    
#     #id = asset id
#     print("User {} hat item aus dem fach herausgenommen".format(UserID))
#     hwCheckOUT.hardwareCeckout(UserID,assetID)
#     closeSF()
#     return True




def sendMsgPutToTerminal(): return

def getAssetIDFromQRScanner(): return "00002"

def openSF(): print("Schließfach öffnen")
def closeSF(): print("Schließfach schließen")

#for user in myReq.getDeployedUsers():
#    addOrderNextFreeSfFor(user)


# Tests
print(boxAndCollectors)
print("======================")
addOrderNextFreeSfFor(userRFID)
print("======================")
print(boxAndCollectors)
print("======================")
#userTakesItem(userRFID)
print("======================")
print(boxAndCollectors)
print(temp)

