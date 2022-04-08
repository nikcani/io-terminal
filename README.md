# Smart Inventory

![key visual](https://raw.githubusercontent.com/nikcani/smart-inventory/main/key-visual.png)


## Abstract
Das Smart Inventory System ermöglicht die schnelle und sichere Inventarisierung unterschiedlichster Objekte. Es ermöglicht die geordnete Ablage, einen guten Überblick und einen schnellen Zugriff. Jegliche Transaktion wird protokolliert und ist einer Person zugeordnet. Das System ist schnell, robust und einfach in der Handhabung.

## Architecture
[back to wiki](https://github.com/nikcani/smart-inventory/wiki#architektur)
```mermaid
graph TD;
A[fa:fa-database Database];
B[fa:fa-barcode Code Scanner];
C[fa:fa-user User];
D[fa:fa-desktop Device with Webbrowser];
E[fa:fa-microchip NFC Scanner];
B-->|HTTP/REST|A;
D-->|fetches data from|A;
C-->|uses|B;
C-->|interacts with|D;
C-->|authorizes at|E;
E-->|activates user session|B;
```

## Documentation
Please have a look at the [Wiki](https://github.com/nikcani/smart-inventory/wiki)
