import requests
from dotenv import load_dotenv
import os

load_dotenv('.\snipe-it.env')

url = 'https://snipe-it.nikcani.de/api/v1/manufacturers'
token= "Bearer " + os.getenv('API_TOKEN')

headers = {"Accept": "application/json",
            "Content-Type":"application/json",
            "Authorization": token}

payload = {"name": "Abdus geile Manufucktur"}

res = requests.post(url, json=payload,headers=headers)
print(res)