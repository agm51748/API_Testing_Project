# Гульнара Абетова, 24 кагорта - Финальный проект. Инженер по тестированию.
import pytest
from sender_stand_request import create_order, track_order

def test_track_order():
    """
    Тест проверяет, что созданный заказ можно успешно отследить.
    """
    # Создаем заказ и получаем номер трека
    order_response = create_order()
    assert order_response.status_code == 201, "Failed to create order"
    track_number = order_response.json().get("track")
    assert track_number, "Track number not found in the response"

    # Отслеживаем заказ по номеру
    response = track_order(track_number)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    response_data = response.json()

    # Проверяем, что ответ содержит ключ "order" и в нем есть "status"
    assert "order" in response_data, "Response does not contain 'order'"
    order_data = response_data["order"]
    assert "status" in order_data, "Order data does not contain 'status'"
    assert order_data["status"] == 0, f"Unexpected order status: {order_data['status']}"