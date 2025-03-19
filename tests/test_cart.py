import pytest
from pages.product import Product
from pages.cart import Cart


@pytest.fixture
def product():
    # фикстура для создания тестового продукта
    return Product(name="Test Product", price=100, description="A test product", category="Category A")


@pytest.fixture
def cart():
    # фикстура для создания тестовой корзины
    return Cart()


def test_add_product_to_cart(cart, product):
    cart.add_product(product)
    assert len(cart.items) == 1  # корзина должна содержать один товар
    assert cart.items[0].name == "Test Product"  # проверяем что это тот же товар
    assert cart.total_price() == 100  # проверяем что цена корзины правильная


def test_remove_product_from_cart(cart, product):
    cart.add_product(product)
    cart.remove_product(product)
    assert len(cart.items) == 0  # корзина должна быть пустой
    assert cart.total_price() == 0  # общая цена должна быть 0
