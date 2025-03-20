# класс для товара
class Product:
    def __init__(self, name, price, description, category):
        # валидации данных
        if price <= 0:
            raise ValueError("Цена товара должна быть больше нуля")
        if not isinstance(name, str) or not name:
            raise ValueError("Имя товара должна быть строкой и не может быть пустым")
        if not isinstance(description, str):
            raise ValueError("Описание товара должна быть строкой")
        if not isinstance(category, str):
            raise ValueError("Категория товара должна быть строкой")

        # атрибуты объекта, которые будут хранить значения, переданные при создании объекта
        self.name = name
        self.price = price
        self.description = description
        self.category = category

    # метод изменения цены
    def update_price(self, new_price):
        if new_price <= 0:
            raise ValueError("Цена должна быть больше нуля")
        self.price = new_price

    # метод изменения описания
    def update_description(self, new_description):
        self.description = new_description

    # метод конвертации объекта в словарь
    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "category": self.category
        }

    # метод сравнения товаров по цене
    def is_more_expensive_than(self, other_product):
        if self.price > other_product.price:
            return True
        return False

    def __str__(self):
        return f"{self.name} - {self.price} KZT"
