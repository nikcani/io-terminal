# Smart Inventory

![key visual](https://raw.githubusercontent.com/nikcani/smart-inventory/main/key-visual.png)


## Abstract
Das Smart Inventory System ermöglicht die schnelle und sichere Inventarisierung unterschiedlichster Objekte. Es ermöglicht die geordnete Ablage, einen guten Überblick und einen schnellen Zugriff. Jegliche Transaktion wird protokolliert und ist einer Person zugeordnet. Bei der Ausleihe und Rückgabe wird über ein Pick-by-light System Schnelligkeit und Ordnung garantiert.

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
