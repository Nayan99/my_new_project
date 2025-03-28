# для заказа, который будет содержать информацию о корзине, пользователе, способах оплаты и доставки
class Order:
    def __init__(self, cart, user, payment_strategy, shipping_strategy):
        # проверяем не пустая ли корзина
        if not cart.items:
            raise ValueError("Корзина не может быть пустой!")
        self.cart = cart
        self.user = user
        self.payment_strategy = payment_strategy
        self.shipping_strategy = shipping_strategy

    # метод для оформления заказа
    def checkout(self):
        # Рассчитываем общую стоимость заказа и осуществляем оплату
        total_amount = self.cart.total_price() + self.shipping_strategy.calculate_shipping()

        # выводим информацию о заказе
        print(f"Заказ от {self.user.name}:")
        print(f"Товары в корзине: {len(self.cart.items)}")
        print(f"Общая стоимость товаров: {self.cart.total_price()} KZT")
        print(f"Способ доставки: {self.shipping_strategy.__class__.__name__}")
        print(f"Стоимость доставки: {self.shipping_strategy.calculate_shipping()} KZT")
        print(f"Общая сумма: {total_amount} KZT")

        # выполняем оплату с выбранной стратегией
        self.payment_strategy.pay(total_amount)

        return total_amount
