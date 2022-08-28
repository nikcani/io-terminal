import requests
from dotenv import load_dotenv
import os

load_dotenv('.\snipe-it.env')

url = 'https://snipe-it.nikcani.de/api/v1/hardware'
token= "Bearer " + os.getenv('API_TOKEN')

headers = {"Accept": "application/json",
            "Content-Type":"application/json",
            "Authorization": token}

payload = { "status_id": "2",
            "model_id":"1",
            "name":"Abdus geile hardware"
}

res = requests.post(url, json=payload,headers=headers)
print(res)