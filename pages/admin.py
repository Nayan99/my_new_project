# для админ-панели, которая будет управлять товарами и заказами
class Admin:
    def __init__(self, name):
        self.name = name
        self.products = []

    # метод для добавления нового товара в список продуктов
    def add_product(self, product):
        self.products.append(product)

    # метод для удаления товара из списка продуктов
    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    # метод для вывода всех продуктов
    def view_product(self):
        return [str(product) for product in self.products]

