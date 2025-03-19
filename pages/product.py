# класс для товара
class Product:
    def __init__(self, name, price, description, category):
        # атрибуты объекта, которые будут хранить значения, переданные при создании объекта
        self.name = name
        self.price = price
        self.description = description
        self.category = category

    def __str__(self):
        return f"{self.name} - {self.price} KZT"
