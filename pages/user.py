# класс для пользователя, который будет хранить информацию о пользователе и его заказах
from pages.order import Order


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        # список заказов пользователя
        self.orders = []

    # метод который возвращает строковые представление пользователя
    def __str__(self):
        return f"{self.name} ({self.email})"

    # метод для создания нового заказа
    def place_order(self, cart, payment_method, delivery_method):
        order = Order(cart, self, payment_method, delivery_method)
        self.orders.append(order)
        return order
