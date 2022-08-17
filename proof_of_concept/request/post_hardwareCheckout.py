import json
import requests

def hardwareCeckout(userID,id):
    url = "https://snipe-it.nikcani.de/api/v1/hardware/{}/checkout".format(id)

    users = json.loads(getUsers())['rows']
    for user in users:
        if user['username'] == userID:
            userID = user['id']

    print("userID: " + str(userID))

    payload = {
        "checkout_to_type": "user",
        "assigned_user": userID,
        "status_id": 7
    }

    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer "+ 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNGE0ZWU3ZGQ1NWM5NGVhZWQ4NjA0MmVkYjRiZmQzYzAxYjUzYWYyMmM1Mzg2NmYyNjY5ZjJkYmFhOTIxZWMxMjA2ZjhkODI5NmEwMmVmNzQiLCJpYXQiOjE2NTU4OTIyNTkuMjk1NTgzLCJuYmYiOjE2NTU4OTIyNTkuMjk1NTg0LCJleHAiOjIxMjkyNzc4NTkuMjkwNTM5LCJzdWIiOiIxIiwic2NvcGVzIjpbXX0.mn33Lp92PdEXDvnFrb8ZFNLaBI4T1YsO4BTNXjilW_UPcrR0JjboXWgl-_NDBZJbwLN1J39kHbAPbZtqsqmdNng0Wg0SVyL5mFVFlbYVkRUw00YUMB-Zt02Ngi4W964OusMfewNFiluhoOBCJm7m6R7uks3vZyFvjfKLnrhPAOqJCHd1hjHtaXMHnCoLv4s67gIvdF1xeLxVLGr520nI7Hj0DXqwSdnqwLnVpI8pmX10bHNF5NKKnSLNgkjJNCshXNIjSHEgxeXXpDWYGx9QTOH1u4qPi3mbxORbQ0fVJCNqTBXbFwmlfTIzoxG4gM6gaBVfMqyC9PUOk20k8Va1aiwMqKkr7HtiPOm_Ivl9rwc06C0lMvEbppfsWUcULjBl4w65I-OoU4WuYCA7LkZa1wkG7_DbSFbMeJjP_9jDgRzg9ifWEwnfdijnijRWyaOwKmc1ydCF8lLwTMQrm7GryKGbTepOeLuzqLK5P4NNpDYUOI9sPXybvUvukb-R9gnwnCwFDibDEpThttLwE82Wq8lXBmsUJdWtNF2p7-Ai7oDcJaDBnRPmX1XKgqPTuL6XMHD-huan47jPz5K8EFKci-BEG9aDvR-NgvWxnyeXz3xlBwrVY2Gvx5TrFe5uJHezWsFt7O4cnMnNk6K70vts744n4g_yob8sZrExsjHGhWs',
        "Content-Type": "application/json"

    }
    response = requests.post(url, json=payload, headers=headers)
    print(response.text)




def getUsers():
    url = 'https://snipe-it.nikcani.de/api/v1/users'
    token= "Bearer " + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNGE0ZWU3ZGQ1NWM5NGVhZWQ4NjA0MmVkYjRiZmQzYzAxYjUzYWYyMmM1Mzg2NmYyNjY5ZjJkYmFhOTIxZWMxMjA2ZjhkODI5NmEwMmVmNzQiLCJpYXQiOjE2NTU4OTIyNTkuMjk1NTgzLCJuYmYiOjE2NTU4OTIyNTkuMjk1NTg0LCJleHAiOjIxMjkyNzc4NTkuMjkwNTM5LCJzdWIiOiIxIiwic2NvcGVzIjpbXX0.mn33Lp92PdEXDvnFrb8ZFNLaBI4T1YsO4BTNXjilW_UPcrR0JjboXWgl-_NDBZJbwLN1J39kHbAPbZtqsqmdNng0Wg0SVyL5mFVFlbYVkRUw00YUMB-Zt02Ngi4W964OusMfewNFiluhoOBCJm7m6R7uks3vZyFvjfKLnrhPAOqJCHd1hjHtaXMHnCoLv4s67gIvdF1xeLxVLGr520nI7Hj0DXqwSdnqwLnVpI8pmX10bHNF5NKKnSLNgkjJNCshXNIjSHEgxeXXpDWYGx9QTOH1u4qPi3mbxORbQ0fVJCNqTBXbFwmlfTIzoxG4gM6gaBVfMqyC9PUOk20k8Va1aiwMqKkr7HtiPOm_Ivl9rwc06C0lMvEbppfsWUcULjBl4w65I-OoU4WuYCA7LkZa1wkG7_DbSFbMeJjP_9jDgRzg9ifWEwnfdijnijRWyaOwKmc1ydCF8lLwTMQrm7GryKGbTepOeLuzqLK5P4NNpDYUOI9sPXybvUvukb-R9gnwnCwFDibDEpThttLwE82Wq8lXBmsUJdWtNF2p7-Ai7oDcJaDBnRPmX1XKgqPTuL6XMHD-huan47jPz5K8EFKci-BEG9aDvR-NgvWxnyeXz3xlBwrVY2Gvx5TrFe5uJHezWsFt7O4cnMnNk6K70vts744n4g_yob8sZrExsjHGhWs'

    headers = {"Accept": "application/json",
                "Content-Type":"application/json",
                "Authorization": token}
    response = requests.get(url, headers=headers)
    return response.text
