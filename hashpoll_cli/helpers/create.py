import requests

def create_help(question: str, option1: str, option2: str, option3: str, option4: str):
    data_to_send = {"question": question, "option1": option1, "option2": option2, "option3": option3, "option4": option4}
    response = requests.post("https://hashapi.hackersreboot.tech/create", json=data_to_send)
    if response.status_code == 200:
        return response.json()
    return False