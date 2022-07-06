import requests
from dotenv import load_dotenv
import os

load_dotenv('.\snipe-it.env')

url = 'https://snipe-it.nikcani.de/api/v1/models'
token= "Bearer " + os.getenv('API_TOKEN')

headers = {"Accept": "application/json",
            "Content-Type":"application/json",
            "Authorization": token}

payload = { "name": "Abdus geile Modelle",
            "category_id":"1",
            "manufacturer_id":"2"}

res = requests.post(url, json=payload,headers=headers)
print(res)