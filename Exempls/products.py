import requests

base_url = "http://marketwain.pw"
apikey = "apikey"


def load_product():
    with open("PATH TO FILE", "rb", encoding="UTF-8") as file:
        data = {"load_file": file.read()}
        response = requests.get(f"{base_url}/products?apikey={apikey}", data=data)
        print(f"Status-code: {response}, response: {response.json()}")


def get_product():
    response = requests.get(f"{base_url}/products/<product_id>?apikey={apikey}")
    print(f"Status-code: {response}, response: {response.json()}")


def get_sub_product():
    response = requests.get(f"{base_url}/products/sub/<sub_product_id>?apikey={apikey}")
    print(f"Status-code: {response}, response: {response.json()}")


def get_status_session():
    response = requests.get(f"{base_url}/products/status/<session_id>?apikey={apikey}")
    print(f"Status-code: {response}, response: {response.json()}")


def try_buy_product():
    response = requests.get(f"{base_url}/products/buy/<id_>?apikey={apikey}")
    with open("save.zip", "wb", encoding="UTF-8") as file:
        file.write(response.content)
