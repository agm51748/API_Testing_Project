import requests
from configuration import BASE_URL
from data import HEADERS, ORDER_PAYLOAD
def send_order_request(): response = requests.post(f"{BASE_URL}/order", headers=HEADERS, json=ORDER_PAYLOAD))
return response