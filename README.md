# IoTerminal

![key visual](https://raw.githubusercontent.com/nikcani/smart-inventory/main/key-visual.png)


## Abstract
Das IoTerminal ermöglicht es Studierenden der TH-Köln das Abholen von angefragter Hardware aus dem things.moxd.io, ohne das ein Mitarbeiter anwesend seien muss. Ähnlich wie eine Packstation sorgt es für eine einfache Ausleihe und Rückgabe. Hierbei wird über ein Pick-by-light System Schnelligkeit und Ordnung garantiert. Jegliche Transaktion wird protokolliert und ist einer Person zugeordnet. 

## Architecture
[back to wiki](https://github.com/nikcani/smart-inventory/wiki#architektur)
```mermaid
graph TD;
A[fa:fa-database Database];
B[fa:fa-barcode Code Scanner];
C[fa:fa-user User];
D[fa:fa-desktop Device with Webbrowser];
E[fa:fa-wifi NFC Scanner];
F[fa:fa-dolly Product];
G[fa:fa-box Location];
H[fa:fa-microchip LED Controller];
I[fa:fa-lightbulb LEDs];
D---|HTTP|A;
C-->|uses|B;
C-->|interacts with|D;
C-->|authorizes at|E;
E-->|activates user session|B;
B-->|scans|F;
F-->|scanned|B;
B-->|scans|G;
G-->|scanned|B;
B---|HTTP/REST|A;
H-->|controls|I;
B-->|activates location light|H;
```
[edit graph](https://mermaid-js.github.io/mermaid-live-editor/)

## Documentation
Please have a look at the [Wiki](https://github.com/nikcani/smart-inventory/wiki)
