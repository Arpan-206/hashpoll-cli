import requests

def get_responses_help(poll_id: str):
    response = requests.get(f"https://24yl4zi1hh.execute-api.us-east-1.amazonaws.com/get-responses?poll_id={poll_id}")
    if response.status_code == 200:
        return response.json()["poll"]
    return False