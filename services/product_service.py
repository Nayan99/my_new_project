from pages.models import Product
from repositories.product_repository import ProductRepository
from pages.models import Category
from pages.db import SessionLocal

class ProductService:
    def __init__(self):
        self.repo = ProductRepository()

    def list_products(self):
        products = self.repo.get_all()
        for p in products:
            print(f"[{p.id}] {p.name} - {p.price} KZT")

    def create_product(self, name: str, description: str, price: float, category_name: str):
        db = SessionLocal()

        category = db.query(Category).filter_by(name=category_name).first()
        if not category:
            print(f"Категория '{category_name}' не найдена")
            return

        product = Product(name=name, description=description, price=price, category_id=category.id)
        self.repo.create(product)
        print(f"Продукт '{name}' создан")
        db.close()

    def close(self):
        self.repo.close()
