from payment_strategy import PaymentStrategy

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата {amount} KZT через PayPal")
