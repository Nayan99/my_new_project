# для админ-панели, которая будет управлять товарами и заказами
class Admin:
    def __init__(self, name):
        self.name = name
        self.products = []

    # метод для добавления нового товара в список продуктов
    def add_product(self, product):
        self.products.append(product)
        # проверяем на уникальность товар
        if any(p.name == product.name for p in self.products):
            raise ValueError(f"Товар с названием {product.name} уже существует!")

    # метод для удаления товара из списка продуктов
    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    # метод для обновления товара
    def update_product(self, product, new_price=None, new_description=None):
        if product in self.products:
            if new_price:
                product.update_price(new_price)
            if new_description:
                product.update_description(new_description)
        else:
            raise ValueError(f"Товар {product.name} не найден для обновления!")

    # метод для поиска товара по имени
    def find_product_by_name(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

    # метод для подсчета количества товаров
    def count_products(self):
        return len(self.products)

    # метод для вывода всех продуктов
    def view_product(self):
        return [str(product) for product in self.products]

