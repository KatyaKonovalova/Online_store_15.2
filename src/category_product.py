class Category:
    """Класс для представления категории продукта"""
    name = str
    descriptions = str
    goods = list

    # Артибут класса, подсчет количества категорий
    number_of_categories = 0
    # Атрибут класса, подсчет количества уникальных товаров
    number_of_uniq_goods = 0

    def __init__(self, name, description, goods):
        """Метод для инициализации экземпляра класса"""
        self.name = name
        self.descriptions = description
        self.goods = goods

        Category.number_of_categories += 1
        Category.number_of_uniq_goods += len(set(self.goods))


class Product:
    """Класс для представлени продукта"""
    name = str
    description = str
    price = float
    quantity_in_stock = int

    def __init__(self, name, description, price, quantity_in_stock):
        """Метод для инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock


category_1 = Category('Смартфоны', 'Смартфоны, как средство не только коммуникации, но и получение'
                                   ' дополнительных функций для удобства жизни', ['Samsung Galaxy C23 Ultra',
                                                                                  'Iphone 15', 'Xiaomi Redmi Note 11'])
category_2 = Category('Телевизоры', 'Современный телевизор, который позволяет наслаждаться просмотром,'
                                    ' станет вашим другом и помощником', ['55" QLED 4K'])
product_1 = Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)
product_2 = Product('Iphone 15', '512GB, Gray space', 210000.0, 8)
product_3 = Product('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)
product_4 = Product('55" QLED 4K', 'Фоновая подсветка', 123000.0, 7)

print(category_1.name)
print(category_1.descriptions)
print(category_1.goods)
print(product_1.name)
print(product_1.description)
print(product_1.price)
print(product_1.quantity_in_stock)
print(Category.number_of_categories)
print(Category.number_of_uniq_goods)
