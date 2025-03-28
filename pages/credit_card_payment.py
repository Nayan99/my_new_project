from pages.payment_strategy import PaymentStrategy

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата {amount} KZT картой")
