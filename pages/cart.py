# класс для корзины
class Cart:
    def __init__(self):
        # список куда будут добавляться товары
        self.items = []

    # метод для добавления товара в корзину
    def add_product(self, product):
        self.items.append(product)

    # метод для удаления товара из корзины
    def remove_product(self, product):
        if product in self.items:
            self.items.remove(product)

    # метод для подсчета общей стоимости корзины
    def total_price(self):
        return sum(item.price for item in self.items)

    # метод для подсчета количества товаров
    def total_items(self):
        return len(self.items)

    # метод проверки пустой корзины
    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return f"Total: {self.total_price()} KZT"
