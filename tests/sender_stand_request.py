import requests
from configuration import BASE_URL, ORDERS_ENDPOINT, TRACK_ENDPOINT
from data import order_payload

def create_order():
    """
    Функция для отправки POST-запроса на создание заказа.
    """
    url = f"{BASE_URL}{ORDERS_ENDPOINT}"
    response = requests.post(url, json=order_payload)
    return response

def track_order(track_number):
    """
    Функция для отправки GET-запроса на отслеживание заказа.
    """
    url = f"{BASE_URL}{TRACK_ENDPOINT}?t={track_number}"
    response = requests.get(url)
    return response