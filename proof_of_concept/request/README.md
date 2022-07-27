Zum posten von einem Asset müssen folgendes **MINDESTENS EINMAL** vorhanden sein:
unterpunkte müssen vorher existieren

 1. Asset /hardware
    1. firma /companies
       1. name /companies
    2. Model /models
       1. Hersteller /manufacturer
       2. Kategorie /category
    3. Status /statuslabels
       1. Einige sind schon vorhaden. Ich benutze erstmal die.
    4. Lieferant (UI)
       1. Name
    5. Standart-Ort /locations
       1. Standart-Ort /locations (potenzieller endlos loop XD)
       2. Manager (UI)
          1. User /users

Ich habe diese schon mit mindestens einem Objekt befüllt. Das Einfügen von neuer Hardware in das System ist hiermit möglich. In jeder Datei muss "\<API TOKEN STEHT IN DISCORD\>" durch einen eigenen API-KEY oder dem aus dem Discord ersetzt werden. Diese Requests sind nur mit verpflichtenden Feldern gefüllt. Weitere können durch das erweitern des payload jsons hinzugefügt werden.

---
Problem: Das Anlegen eines neuen Users funktioniert nicht. In die Datei post_Users.py schauen.

Problem: In post_Hardware.py darf kein "asset_tag" hinzugefügt werden, da dieser austomatisch befüllt wird. Es funktioniert auch nicht wenn es da ist. Einfach weglassen.
