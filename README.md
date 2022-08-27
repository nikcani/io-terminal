# IoTerminal

![key visual](https://raw.githubusercontent.com/nikcani/smart-inventory/main/key-visual.png)


## Abstract
Das IoTerminal ermöglicht es Studierenden der TH-Köln das Abholen von angefragter Hardware aus dem [things.moxd.io](things.moxd.io), ohne das ein Mitarbeiter anwesend sein muss. Ähnlich wie eine Packstation sorgt es für eine einfache Ausleihe und Rückgabe. Hierbei wird über ein Pick-by-light System Schnelligkeit und Ordnung garantiert. Jegliche Transaktion wird protokolliert und ist einer Person zugeordnet.

## Architecture
[back to wiki](https://github.com/nikcani/smart-inventory/wiki#architektur)
```mermaid
graph TD

USER(fa:fa-user User)

BROWSER[fa:fa-desktop Device with Webbrowser]

SNIPEIT[fa:fa-database SNIPE-IT]

PI[[fa:fa-microchip PI]]
CAMERA[fa:fa-barcode PI Camera]
NFCSCANNER[fa:fa-wifi NFC Scanner]

ESP[[fa:fa-microchip ESP]]
LED[fa:fa-lightbulb LEDs]
BUTTONS[fa:fa-toggle-on Buttons]
DISPLAY[fa:fa-tv Display]
LOCK[fa:fa-lock Lock]

USER-->|interacts with|BROWSER
USER-->|sees|DISPLAY
USER-->|authorizes at|NFCSCANNER
USER-->|presses|BUTTONS
USER-->|uses|CAMERA

DISPLAY-->|presents|USER
LED-->|indicate|USER

BROWSER-->|HTTP Request|SNIPEIT
SNIPEIT-->|HTTP Response|BROWSER

PI-->|HTTP Request|SNIPEIT
SNIPEIT-->|HTTP Response|PI

NFCSCANNER-->|send code|PI
PI-->|request code|NFCSCANNER

CAMERA-->|stream|PI
PI-->|activate|CAMERA

ESP-->|serial bus|PI
PI-->|serial bus|ESP

ESP-->|controls|LED
ESP-->|controls|DISPLAY
ESP-->|controls|LOCK

BUTTONS-->|interrupt|ESP
```
[edit graph](https://mermaid-js.github.io/mermaid-live-editor/)

## Documentation
Please have a look at the [Wiki](https://github.com/nikcani/smart-inventory/wiki)
