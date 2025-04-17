from pages.db import SessionLocal
from services.cart_service import CartService
from pages.models import User
from pages.models import Product, Category

def main():
    user_id = 1
    cart_service = CartService()

    db = SessionLocal()

    user = db.query(User).filter_by(id=user_id).first()

    if not user:
        print(f"Пользователь с ID {user_id} не найден. Создаем нового пользователя.")
        user = User(name="Клава Кока", email="clavacoca@gmail.com", password_hash="password")
        db.add(user)
        db.commit()
        db.refresh(user)
        print(f"Пользователь с ID {user.id} создан")

    product = db.query(Product).filter_by(id=1).first()

    if not product:
        print("Продукта с ID=1 нет. Создаём новый.")
        category = db.query(Category).first()  # Проверим, есть ли хотя бы одна категория
        if not category:
            print("Нет категорий в базе. Создаём тестовую категорию.")
            category = Category(name="Test Category")
            db.add(category)
            db.commit()
            db.refresh(category)
            print(f"Категория с ID={category.id} добавлена.")

        product = Product(
            id=1,
            name="Test Product",
            description="Test Product Description",
            price=1000.0,
            category_id=category.id
        )
        db.add(product)
        db.commit()
        db.refresh(product)
        print(f"Продукт с ID={product.id} добавлен.")

    cart_service.add_product_to_cart(user_id, 1, 2)
    cart = cart_service.get_cart_for_user(user_id)

    print("Корзина:")
    for item in cart.items:
        print(f"{item.name} - {item.price} KZT")
    print(cart)

    cart_service.close()

if __name__ == "__main__":
    main()
