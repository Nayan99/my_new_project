from pages.shipping_strategy import ShippingStrategy

class StandardShipping(ShippingStrategy):
    def calculate_shipping(self):
        return 5  # Стоимость стандартной доставки
