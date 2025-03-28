# для заказа, который будет содержать информацию о корзине, пользователе, способах оплаты и доставки
class Order:
    def __init__(self, cart, user, payment_strategy, shipping_strategy):
        self.cart = cart
        self.user = user
        self.payment_strategy = payment_strategy
        self.shipping_strategy = shipping_strategy

    # метод для оформления заказа
    def checkout(self):
        # Рассчитываем общую стоимость заказа и осуществляем оплату
        total_amount = self.cart.total_price() + self.shipping_strategy.calculate_shipping()
        print(f"Общая сумма: {total_amount} KZT")
        self.payment_strategy.pay(total_amount)
