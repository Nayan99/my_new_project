from pages.shipping_strategy import ShippingStrategy

class ExpressShipping(ShippingStrategy):
    def calculate_shipping(self):
        return 20  # Стоимость экспресс-доставки
