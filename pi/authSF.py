# ein pair besteht aus einem/einer schliesßfach/-nummer ((links) in dem fall von 1-6) und der ID des Users (rechts)
# ist die ID leer dann ist das schließfach auch leer
# man kann durch ein hinzufügen eines dritten elements auch den inhalt des schließfaches einbetten erfordert aber kleine modifikationen im code

def getUserIDFormRFID(): return "Abdurrahman"   # psydo RFID

SFsAndIDs = [(1,"Lisa"),(2,"Fuhrmann"),(3,"Niklas"),(4,"Canisius"),(5,""),(6,"Karakan")]
temp = SFsAndIDs # testing || Orginal zustand der liste

abdu = getUserIDFormRFID()

# suche nach dem NÄCHSTEN FREIEN platz
def isThereSpace():
    for sf , id in SFsAndIDs:
        if(id == ""):
            print("Nächstes freie Schließfach ist {}".format(sf))
            return sf
    print("Schließfächer alle voll")
    return False

# suche nach dem SF für den einen user
def whereUserItem(UserID):
    for sf , id in SFsAndIDs:
        if(id == UserID):
            print("Die Order des Users {} ist im Schließfach NR.: {}".format(UserID, sf))
            return sf
    print("Order leider nicht vorhanden")
    return False

def addOrderNextFreeSfFor(UserID):
    sf = isThereSpace()
    if not (sf):
        print ("Alle Schließfächer sind voll")
        return False
    openSF()
    SFsAndIDs[sf-1] = (sf,UserID) #-1 weil ein array fängt bei 0 an, duh
    sendMsgPutToTerminal()
    closeSF()
    print ("Die Bestellung des Users {} wurde in das Schließfach {} hinzugefügt".format(UserID,sf))
    return True


def userTakesItem(UserID):
    sf = whereUserItem(UserID)
    if not (sf): 
        print("Item nicht im Schließfach.")
        return False
    openSF()
    SFsAndIDs[sf-1] = (sf,"") # Mereke: Leere ID = Kein Item
    sendMsgTakenToTerminal()
    closeSF()
    return True




def openSF(): print("Schließfach öffnen")
def sendMsgTakenToTerminal(): print("User hat item aus dem fach herausgenommen") # potenzielle erweiterung notwendig e.g. druckplatte
def sendMsgPutToTerminal(): print("User hat item ins fach gelegt") # potenzielle erweiterung notwendig e.g. druckplatte
def closeSF(): print("Schließfach schließen")




# Tests
print(SFsAndIDs)
print("======================")
addOrderNextFreeSfFor(abdu)
print("======================")
print(SFsAndIDs)
print("======================")
userTakesItem(abdu)
print("======================")
print("======================")
print(SFsAndIDs)
print(temp)

