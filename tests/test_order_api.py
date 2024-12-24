# Гульнара Абетова, 24 кагорта - Финальный проект. Инженер по тестированию.
import requests
from configuration import BASE_URL, HEADERS
def test_create_and_get_order():
    # Параметры заказа
    order_payload = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": ["BLACK"]
     }
    # Cоздание заказа
    response = requests.post(f"{BASE_URL}/api/v1/orders", json=order_payload, headers=HEADERS)
    assert response.status_code == 201, f"Не удалось создать заказ: {response.status_code}, {response.text}"
    # Получаем трек-номер
    track_namber = response.json().get("track")
    assert track_namber, "Трек-номер отсутствует в ответе"
    # Проверяем получение заказа по трек-номеру
    response = requests.get(f"{BASE_URL}/api/v1/orders/track?t={track_namber}")
    assert response.status_code == 200, f"Не удалось получить заказ: {response.status_code}, {response.text}"
    print("Тест успешно завершён!")

