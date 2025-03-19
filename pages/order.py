# для заказа, который будет содержать информацию о корзине, пользователе, способах оплаты и доставки
class Order:
    def __init__(self, cart, user, payment_method, delivery_method):
        self.cart = cart
        self.user = user
        self.payment_method = payment_method
        self.delivery_method = delivery_method

    # метод для оформления заказа
    def checkout(self):
        print(f"Заказ сделан {self.user.name} !")
        print(f"Общая цена {self.cart.total_price()} KZT")
        print(f"Способ оплаты {self.payment_method}")
        print(f"Способ доставки {self.delivery_method}")
