import requests

def vote_help(poll_id: str, option: int):
    if option not in [1, 2, 3, 4]:
        raise ValueError("Option must be 1, 2, 3, 4")
    data_to_send = {"poll_id": poll_id, "vote": option}
    response = requests.post("https://24yl4zi1hh.execute-api.us-east-1.amazonaws.com/vote", json=data_to_send)
    if response.status_code == 200:
        return True
    return False