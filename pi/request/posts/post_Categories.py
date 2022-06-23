import requests

url = 'https://snipe-it.nikcani.de/api/v1/categories'
token= "Bearer <API TOKEN STEHT IN DISCORD>"

headers = {"Accept": "application/json",
            "Content-Type":"application/json",
            "Authorization": token}

payload = { "name": "Abdus geile Kategorie",
            "category_type": "asset"}
            # category_type nur: "asset", "accessory", "consumable", "component"

res = requests.post(url, json=payload,headers=headers)
print(res)