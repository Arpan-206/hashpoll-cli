import requests

def get_poll_help(poll_id: str):
    response = requests.get(f"https://hashapi.hackersreboot.tech/get/{poll_id}")
    if response.status_code == 200:
        return response.json()["poll"]
    return False