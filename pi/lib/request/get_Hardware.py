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
    myrows = json_object["rows"]
    for row in myrows:
        if (row['assigned_to']) is not None:
                # myListe.append(row['assigned_to']['username'])
                print(row['assigned_to']['username'])
                print("============================")
                objectIDAndUser = (row['assigned_to']['username'],row['id'],)
                myListe.append(objectIDAndUser)
    print(myListe)
    return myListe