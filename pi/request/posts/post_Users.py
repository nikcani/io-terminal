# funktioniert gerade nicht weil keine ahnung auch keine lust das gerade rauszufinden denn es ist 01:54 uhr morgens und ich denke mir "warum mache ich das? ich habe doch sooooo viel zeit, abdurrahman du, erstens hast einen super langen namen und zweitens führst hier gerade selbstgespräche in textform nur damit das deine kommulitonen lesen und sich denken "ist dieser typ behindert?" und meine antwort darauf wird nur sein "vielleicht" " und jetzt geh schlafen du idiot. ja ciao leute, VOLL-METAAAAA
import requests

url = 'https://snipe-it.nikcani.de/api/v1/models'
token= "Bearer <API TOKEN STEHT IN DISCORD>"

headers = {"Accept": "application/json",
            "Content-Type":"application/json",
            "Authorization": token}

payload = { "first_name": "Abdurrahman",
            "last_name":" der geile Typ", #optional
            "username": "akarakan",
            "password":"password",
            "password_confirmation":"password" # muss password 100% Matchen
            }

res = requests.post(url, json=payload,headers=headers)
print(res)