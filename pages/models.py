from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Text, TIMESTAMP
from sqlalchemy.orm import relationship
from datetime import datetime
from pages.db import Base

# Модель для пользователей
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

    orders = relationship('Order', back_populates='user')
    carts = relationship('Cart', back_populates='user')

# Модель для категорий товаров
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)

    products = relationship('Product', back_populates='category')

# Модель для продуктов
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(Text)
    price = Column(DECIMAL(10, 2), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    category = relationship('Category', back_populates='products')
    cart_items = relationship('CartItem', back_populates='product')
    order_items = relationship('OrderItem', back_populates='product')

# Модель для корзин
class Cart(Base):
    __tablename__ = 'carts'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='carts')
    cart_items = relationship('CartItem', back_populates='cart')

# Модель для товаров в корзине
class CartItem(Base):
    __tablename__ = 'cart_items'

    id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(Integer, ForeignKey('carts.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, default=1, nullable=False)

    cart = relationship('Cart', back_populates='cart_items')
    product = relationship('Product', back_populates='cart_items')

# Модель для заказов
class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    total_price = Column(DECIMAL(10, 2), nullable=False)
    payment_status = Column(String(50))
    shipping_status = Column(String(50))
    payment_method_id = Column(Integer, ForeignKey('payment_methods.id'), nullable=False)
    shipping_method_id = Column(Integer, ForeignKey('shipping_methods.id'), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    user = relationship('User', back_populates='orders')
    payment_method = relationship('PaymentMethod', back_populates='orders')
    shipping_method = relationship('ShippingMethod', back_populates='orders')
    order_items = relationship('OrderItem', back_populates='order')

# Модель для методов оплаты
class PaymentMethod(Base):
    __tablename__ = 'payment_methods'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)

    orders = relationship('Order', back_populates='payment_method')

# Модель для методов доставки
class ShippingMethod(Base):
    __tablename__ = 'shipping_methods'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    cost = Column(DECIMAL(10, 2), nullable=False)

    orders = relationship('Order', back_populates='shipping_method')

# Модель для элементов заказа
class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)

    order = relationship('Order', back_populates='order_items')
    product = relationship('Product', back_populates='order_items')
