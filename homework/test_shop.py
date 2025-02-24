"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart(product):
    cart = Cart()  # Создаём объект Cart
    cart.add_product(product)  # Добавляем продукт в корзину
    return cart

@pytest.fixture
def product1():
    return Product("notebook", 200, "This is a notebook", 500)



class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1000) is True
        assert all(product.check_quantity(i) for i in range(1, 1000)) is True
        assert product.check_quantity(1001) is False


    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(100)
        assert product.quantity == 900


    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(product.quantity + 1)

class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self , cart , product1):
        cart.add_product(product1, 10)
        assert cart.add_product(product1) == 10

    def test_remove_product(self, cart , product1):
        cart.add_product(product1, 5)

        cart.remove_product(product1, 5)
        assert cart.add_product(product1) == 0

    def test_full_remove(self, cart , product1):
        cart.remove_product(product1)
        assert product1 not in cart.products

    def test_clear(self, cart, product1):
        cart.add_product(product1, 2)

        # Очищаем корзину
        cart.clear()
        assert len(cart.products) == 0

    def test_buy(self, cart, product1):
         cart.add_product(product1, 10)
         cart.add_product(product1, 10)
         assert cart.get_total_price() == 4000

    def test_buy_value(self, cart, product1):
        cart.add_product(product1, 10)
        cart.buy()
        assert product1.quantity == 490

        assert len(cart.products) == 0

    def test_buy_with_insufficient_stock(self, cart, product1):
        cart.add_product(product1, 700)

        # Покупка должна вызвать ValueError из-за недостатка товара
        with pytest.raises(ValueError, match=f"Товара '{product1.name}' недостаточно на складе!"):
            cart.buy()














