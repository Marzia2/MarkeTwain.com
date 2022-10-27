import requests

base_url = "http://marketwain.pw"
apikey = "apikey"


def get_my_account():
    response = requests.get(f"{base_url}/users?apikey={apikey}")
    print(f"Status-code: {response}, response: {response.json()}")


def refresh_apikey():
    response = requests.get(f"{base_url}/users/refresh_apikey?apikey={apikey}")
    print(f"Status-code: {response}, response: {response.json()}")

