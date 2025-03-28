from pages.product import Product


class ProductFactory:
    @staticmethod
    def create_product(name, price, description, category):
        if not name or not isinstance(name, str):
            raise ValueError("Название продукта должно быть строкой и не может быть пустым")
        if price <= 0:
            raise ValueError("Цена должна быть больше нуля")
        if not isinstance(description, str):
            raise ValueError("Описание должно быть строкой")
        if not isinstance(category, str):
            raise ValueError("Категория должна быть строкой")

        # возвращаем новый объект Product
        return Product(name, price, description, category)
