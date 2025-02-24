from dataclasses import dataclass
from itertools import product


@dataclass
class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        return self.quantity >= quantity


    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if self.check_quantity(quantity):
            self.quantity -= quantity
        else:
            raise ValueError (f'Недостаточно {self.name} на складе')


    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=0):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count

            # Возвращаем текущее количество товара в корзине
        return self.products[product]


    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if product not in self.products:
            return

        if remove_count is None or remove_count >= self.products[product]:
            del self.products[product]
        else:
            self.products[product] -= remove_count



    def clear(self):
        self.products.clear()


    def get_total_price(self) -> float:
        total_price = 0.0
        for product , quantity in self.products.items():
            total_price = product.price * quantity
        return total_price


    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        if not self.products:  # Проверка на пустую корзину
            raise ValueError("Корзина пуста, нечего покупать!")

            # Проверка наличия достаточного количества товара на складе
        for product, quantity in self.products.items():
            if product.quantity < quantity:
                raise ValueError(f"Товара '{product.name}' недостаточно на складе!")

            # Уменьшаем количество товара на складе
        for product, quantity in self.products.items():
            product.quantity -= quantity

            # Очистка корзины после успешной покупки
        self.products.clear()

