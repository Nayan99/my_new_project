# класс для пользователя, который будет хранить информацию о пользователе и его заказах
import hashlib

from pages.order import Order


class User:
    def __init__(self, name, email, password):
        # валидация email
        if "@" not in email or "." not in email:
            raise ValueError("Некорректный email")

        self.name = name
        self.email = email
        self.password = self.hash_password(password)
        # список заказов пользователя
        self.orders = []

    # метод хеширования пароля
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    # метод который возвращает строковые представление пользователя
    def __str__(self):
        return f"{self.name} ({self.email})"

    # метод для создания нового заказа
    def place_order(self, cart, payment_method, delivery_method):
        order = Order(cart, self, payment_method, delivery_method)
        self.orders.append(order)
        return order

    # метод получения всех заказов пользователя
    def get_orders(self):
        return self.orders

    # метод для отмены заказа
    def cancel_order(self, order):
        if order in self.orders:
            self.orders.remove(order)
            return f"Заказ {order} был отменен"
        else:
            return "Заказ не найден"
