import requests

url = 'https://snipe-it.nikcani.de/api/v1/models'
token= "Bearer <API TOKEN STEHT IN DISCORD>"

headers = {"Accept": "application/json",
            "Content-Type":"application/json",
            "Authorization": token}
response = requests.get(url, headers=headers)
print(response.text)