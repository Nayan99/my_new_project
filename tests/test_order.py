from pages.product import Product
from pages.cart import Cart
from pages.user import User
from pages.order import Order
import pytest


@pytest.fixture
def user():
    return User(name="Nayan Bayanych", email="bayanych@bayan.com", password="password123")


@pytest.fixture
def product():
    return Product(name="Test Product", price=100, description="A test product", category="Category A")


@pytest.fixture
def cart(product):
    cart = Cart()
    cart.add_product(product)
    return cart


def test_place_order(cart, user):
    order = user.place_order(cart, payment_method="Credit Card", delivery_method="Standard Shipping")
    assert len(user.orders) == 1  # у пользователя должен быть один заказ
    assert order.cart == cart  # заказ должен содержать ту же корзину
    assert order.user == user  # заказ должен быть связан с пользователем
    assert order.payment_method == "Credit Card"  # проверяем способ оплаты
    assert order.delivery_method == "Standard Shipping"  # проверяем способ доставки
