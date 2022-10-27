import requests

base_url = "http://marketwain.pw"
apikey = "apikey"


def get_catalog():
    response = requests.get(f"{base_url}/catalog?apikey={apikey}&skip=0&limit=10")
    print(f"Status-code: {response}, response: {response.json()}")


def get_sub_catalog():
    response = requests.get(f"{base_url}/catalog/<service_id>?apikey={apikey}&skip=0&limit=10")
    print(f"Status-code: {response}, response: {response.json()}")


def get_sub_catalog_with_filter():
    response = requests.get(f"{base_url}/catalog/<service_id>?apikey={apikey}&skip=0&limit=10&min_price=10&max_price=30")
    print(f"Status-code: {response}, response: {response.json()}")
