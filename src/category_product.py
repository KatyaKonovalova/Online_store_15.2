from abc import ABC, abstractmethod


class MixinOutput:
    def __init__(self):
        print('Объект создан')

    def print_repr(self):
        print(repr(self))


class Category(MixinOutput):
    """Класс для представления категории продукта"""
    name = str
    description = str
    goods_list = list

    # Артибут класса, подсчет количества категорий
    number_of_categories = 0
    # Атрибут класса, подсчет количества уникальных товаров
    number_of_uniq_goods = 0

    def __init__(self, name, description, goods_list):
        """Метод для инициализации экземпляра класса"""
        super().__init__()
        self.name = name
        self.description = description
        self.__goods_list = goods_list
        self.__goods = {}

        Category.number_of_categories += 1
        Category.number_of_uniq_goods += len(set(self.__goods_list))

    def __repr__(self):
        return f'Category({self.name}, {self.description}, {self.__goods})'

    def add_product(self, *prods):
        """Добавление нового товара в список. Если такой товар уже есть в self.__goods, выбирается  наибольшее значение
        цены и скалдывается значение товаров в наличии"""
        """self.__goods - словарь{Название товара(name): данные о товаре(name, description, price, 
        quantity_in_stock)} """
        for new_prod in prods:
            if not isinstance(new_prod, Product):
                continue
            if new_prod.name in self.__goods:
                stored_product = self.__goods[new_prod.name]
                self.__goods[new_prod.name] = Product(new_prod.name, new_prod.description,
                                                      max(new_prod.price, stored_product.price),
                                                      new_prod.quantity_in_stock + stored_product.quantity_in_stock)
            else:
                self.__goods[new_prod.name] = new_prod

    @property
    def get_goods_list(self, __goods_list):
        return self.__goods[__goods_list]

    def get_product_by_name(self, name: str):
        return self.__goods[name]

    def counting_goods(self):
        """Подсчет числа уникальных товаров в списке"""
        return len(self.__goods)

    @property
    def products(self):
        """Вывод товаров содержащихся в словаре self.__goods в нужном формате"""
        result = f'\nКатегория: {self.name}\n'
        for prod in self.__goods.values():
            result += f'{prod}\n'
        return result

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self)} шт.'

    def __len__(self):
        """Общее количество всех товаров категории на складе"""
        all_quantity = 0
        for prod in self.__goods.values():
            all_quantity += prod.quantity_in_stock
        return all_quantity


class AbstractProduct(ABC):

    @abstractmethod
    def demonstrate_abilities(self):
        pass


class Product(AbstractProduct, MixinOutput):
    """Класс для представлени продукта"""
    name = str
    description = str
    price_ = float
    quantity_in_stock = int

    def __init__(self, name, description, price, quantity_in_stock):
        """Метод для инициализации экземпляра класса"""
        super().__init__()
        self.name = name
        self.description = description
        self.__price = price
        self.quantity_in_stock = quantity_in_stock

    def __repr__(self):
        return f'Product({self.name}, {self.description}, {self.__price}, {self.quantity_in_stock})'

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity_in_stock} шт.'

    def demonstrate_abilities(self):
        return 'Я продукт'

    @classmethod
    def new_good(cls, name, description, price, quantity_in_stock):
        """Создание нового товара. @classmethod используем, чтобы нам провести инициализацию"""
        return cls(name, description, price, quantity_in_stock)

    @property
    def price(self):
        """"Геттер, возвращающий цену товара"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер, присваивающий цену товару в зависимости от условий"""
        if new_price <= 0:
            print('Incorrect price')
            return
        else:
            if self.__price > new_price:
                answer = input(f'Новая цена ниже. Меняем цену? y, n: ')
                if answer == 'y':
                    self.__price = new_price
                elif answer != 'n' and answer != 'y':
                    print('Цена останется прежней')
                else:
                    return
            self.__price = new_price

    def __add__(self, other):
        """Нахождение общей стоимости суммы двух типов товаров на складе"""
        if not isinstance(other, type(self)):
            raise ValueError('Складывать можно только продукты одного класса.')
        else:
            result = self.price * self.quantity_in_stock + other.price * other.quantity_in_stock
            return result


class Smartphone(Product):
    def __init__(self, name, description, price, quantity_in_stock, performance: float, model: str, ram: float,
                 color: str):
        super().__init__(name, description, price, quantity_in_stock)

        self.performance = performance
        self.model = model
        self.ram = ram
        self.color = color

    def demonstrate_abilities(self):
        return 'Включить камеру и сделать селфи'


class Grass(Product):
    def __int__(self, name, description, price, quantity_in_stock, manufacturer_country: str, growth_period: int,
                color: str):
        super().__init__(name, description, price, quantity_in_stock)

        self.manufacturer_country = manufacturer_country
        self.growth_period = growth_period
        self.color = color


category_1 = Category('Смартфоны', 'Смартфоны, как средство не только коммуникации, но и получение'
                                   ' дополнительных функций для удобства жизни', ['Samsung Galaxy C23 Ultra',
                                                                                  'Iphone 15', 'Xiaomi Redmi Note 11'])
category_1.print_repr()
category_2 = Category('Телевизоры', 'Современный телевизор, который позволяет наслаждаться просмотром,'
                                    ' станет вашим другом и помощником', ['55" QLED 4K'])
category_2.print_repr()
product_1 = Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)
product_1.print_repr()
product_2 = Product('Iphone 15', '512GB, Gray space', 210000.0, 8)
product_3 = Product('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)
product_4 = Product('55" QLED 4K', 'Фоновая подсветка', 123000.0, 7)
category_1.add_product(product_1, product_2, product_3)
category_2.add_product(product_4)
print(product_1)
print(category_1)
print(category_1.get_product_by_name('Iphone 15'))

print(category_2.products)
print(category_1.products)
print(product_1.demonstrate_abilities())

# product_5 = Product.new_good('Nokia', '2', 1.0, 5)
# product_6 = Product.new_good('Nokia', '2', 23.0, 8)
# category_1.add_product(product_5, product_6)
#
# product_1.price = float(input('Введите цену: '))
# print(category_1.products)

print(product_1 + product_2)
