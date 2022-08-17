import requests
from dotenv import load_dotenv
import os


def getUsers():
    load_dotenv('.\snipe-it.env')
    url = 'https://snipe-it.nikcani.de/api/v1/users'
    token= "Bearer " + os.getenv('API_TOKEN')

    headers = {"Accept": "application/json",
                "Content-Type":"application/json",
                "Authorization": token}
    response = requests.get(url, headers=headers)
    return response.text