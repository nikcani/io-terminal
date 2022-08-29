import json

import requests

api_url = "https://snipe-it.nikcani.de/api/v1"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNGE0ZWU3ZGQ1NWM5NGVhZWQ4NjA0MmVkYjRiZmQzYzAxYjUzYWYyMmM1Mzg2NmYyNjY5ZjJkYmFhOTIxZWMxMjA2ZjhkODI5NmEwMmVmNzQiLCJpYXQiOjE2NTU4OTIyNTkuMjk1NTgzLCJuYmYiOjE2NTU4OTIyNTkuMjk1NTg0LCJleHAiOjIxMjkyNzc4NTkuMjkwNTM5LCJzdWIiOiIxIiwic2NvcGVzIjpbXX0.mn33Lp92PdEXDvnFrb8ZFNLaBI4T1YsO4BTNXjilW_UPcrR0JjboXWgl-_NDBZJbwLN1J39kHbAPbZtqsqmdNng0Wg0SVyL5mFVFlbYVkRUw00YUMB-Zt02Ngi4W964OusMfewNFiluhoOBCJm7m6R7uks3vZyFvjfKLnrhPAOqJCHd1hjHtaXMHnCoLv4s67gIvdF1xeLxVLGr520nI7Hj0DXqwSdnqwLnVpI8pmX10bHNF5NKKnSLNgkjJNCshXNIjSHEgxeXXpDWYGx9QTOH1u4qPi3mbxORbQ0fVJCNqTBXbFwmlfTIzoxG4gM6gaBVfMqyC9PUOk20k8Va1aiwMqKkr7HtiPOm_Ivl9rwc06C0lMvEbppfsWUcULjBl4w65I-OoU4WuYCA7LkZa1wkG7_DbSFbMeJjP_9jDgRzg9ifWEwnfdijnijRWyaOwKmc1ydCF8lLwTMQrm7GryKGbTepOeLuzqLK5P4NNpDYUOI9sPXybvUvukb-R9gnwnCwFDibDEpThttLwE82Wq8lXBmsUJdWtNF2p7-Ai7oDcJaDBnRPmX1XKgqPTuL6XMHD-huan47jPz5K8EFKci-BEG9aDvR-NgvWxnyeXz3xlBwrVY2Gvx5TrFe5uJHezWsFt7O4cnMnNk6K70vts744n4g_yob8sZrExsjHGhWs"
headers = {
    "Accept": "application/json",
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json"
}


def hardware_change_status(hw_id, status_id):
    payload = {
        "status_id": status_id
    }
    response = requests.patch("{}/hardware/{}".format(api_url, hw_id), json=payload, headers=headers)
    print(response.text)


def hardware_status_set_ready_to_pickup(hw_id): hardware_change_status(hw_id, 4)  # abholbereit


def hardware_status_set_ready_to_return(hw_id): hardware_change_status(hw_id, 5)  # rückgabebereit


def hardware_status_set_picked_up(hw_id): hardware_change_status(hw_id, 7)  # abgeholt


def hardware_checkin(asset_id):  # zurückgegeben
    payload = {
        "status_id": 8
    }
    response = requests.post("{}/hardware/{}/checkin".format(api_url, int(asset_id)), json=payload, headers=headers)
    print(response.text)


def get_assigned_user(asset_id):
    response = requests.get("{}/hardware".format(api_url), headers=headers)
    print(response.text)
    json_object = json.loads(response.text)

    rows = json_object["rows"]
    for row in rows:
        if (row["asset_tag"]) == str(asset_id):
            return row['assigned_to']['username']
    return False
