from repositories.cart_repository import CartRepository
from pages.cart import Cart

class CartService:
    def __init__(self):
        self.repo = CartRepository()

    def get_cart_for_user(self, user_id):
        db_carts, cart_items = self.repo.load_cart(user_id)

        oop_cart = Cart()
        for item in cart_items:
            for _ in range(item.quantity):
                oop_cart.add_product(item.product)

        return oop_cart

    def add_product_to_cart(self, user_id, product_id, quantity=1):
        self.repo.add_to_cart(user_id, product_id, quantity)
        print("Товар добавлен в корзину")

    def remove_product_from_cart(self, user_id, product_id):
        self.repo.remove_from_cart(user_id, product_id)
        print("Товар удален из корзины")

    def close(self):
        self.repo.close()
