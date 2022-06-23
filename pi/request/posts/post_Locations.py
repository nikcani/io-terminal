import requests

url = 'https://snipe-it.nikcani.de/api/v1/locations'
token= "Bearer <API TOKEN STEHT IN DISCORD>"

headers = {"Accept": "application/json",
            "Content-Type":"application/json",
            "Authorization": token}

payload = { "name": "Abdus geiler Ort"}

res = requests.post(url, json=payload,headers=headers)
print(res)