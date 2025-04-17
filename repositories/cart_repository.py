from pages.db import SessionLocal
from pages.models import Cart as DBCart, CartItem, Product

class CartRepository:
    def __init__(self):
        self.db = SessionLocal()

    def load_cart(self, user_id):
        carts = self.db.query(DBCart).filter_by(user_id=user_id).first()
        if not carts:
            cart = DBCart(user_id=user_id)
            self.db.add(cart)
            self.db.commit()
            self.db.refresh(cart)
        items = self.db.query(CartItem).filter_by(cart_id=carts.id).all()
        return carts, items

    def add_to_cart(self, user_id, product_id, quantity=1):
        carts, _ = self.load_cart(user_id)
        existing_item = self.db.query(CartItem).filter_by(
            cart_id=carts.id, product_id=product_id
        ).first()
        if existing_item:
            existing_item.quantity += quantity
        else:
            item = CartItem(cart_id=carts.id, product_id=product_id, quantity=quantity)
            self.db.add(item)
        self.db.commit()

    def remove_from_cart(self, user_id, product_id):
        carts, _ = self.load_cart(user_id)
        item = self.db.query(CartItem).filter_by(
            cart_id=carts.id, product_id=product_id
        ).first()
        if item:
            self.db.delete(item)
            self.db.commit()

    def close(self):
        self.db.close()
