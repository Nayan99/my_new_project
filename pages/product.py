# класс для товара
class Product:
    def __init__(self, name, price, description, category):
        # атрибуты объекта, которые будут хранить значения, переданные при создании объекта
        self._name = None
        self._price = None
        self._description = None
        self._category = None
        self.name = name  # Будет использовать setter
        self.price = price  # Будет использовать setter
        self.description = description  # Будет использовать setter
        self.category = category  # Будет использовать setter

    # Getter и Setter для name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Имя товара должно быть строкой или не может быть пустым")
        self._name = value

    # Getter и Setter для price
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Цена товара должна быть больше нуля")
        self._price = value

    # Getter и Setter для description
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise ValueError("Описание строки должно быть строкой")
        self._description = value

    # Getter и Setter для category
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Категория товара должна быть строкой")
        self._category = value

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
