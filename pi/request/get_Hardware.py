import requests
from dotenv import load_dotenv
import os
import json

def getDeployedUsers():
    load_dotenv('.\snipe-it.env')
    url = 'https://snipe-it.nikcani.de/api/v1/hardware'
    token= "Bearer " + os.getenv('API_TOKEN')

    headers = {"Accept": "application/json",
                "Content-Type":"application/json",
                "Authorization": token}
    response = requests.get(url, headers=headers)

    #print(response.text)


    #check data type with type() method
    #print(type(response.text))

    #convert string to  object
    json_object = json.loads(response.text)

    #check new data type
    #print(json_object["rows"][0]['assigned_to']['username'])

    myListe =[]
    for row in json_object["rows"]:

        if not (row['assigned_to']['username'] is None):
            myListe.append(row['assigned_to']['username'])
            print(row['assigned_to']['username'])
            print("============================")

    return myListe