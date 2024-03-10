import pytest
from src.category_product import Category
from src.category_product import Product


@pytest.fixture
def category_item():
    return Category('Смартфоны', 'Смартфоны, как средство не только коммуникации, '
                                 'но и получение дополнительных функций для удобства жизни')


@pytest.fixture
def product_item():
    return Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)


def test_init_category(category_item):

    assert category_item.name == 'Смартфоны'
    assert category_item.descriptions == ('Смартфоны, как средство не только коммуникации, но и получение '
                                           'дополнительных функций для удобства жизни')
    assert category_item.goods == ['Samsung Galaxy C23 Ultra', 'Iphone 15', 'Xiaomi Redmi Note 11']


def test_init_product(product_item):

    assert product_item.name == 'Samsung Galaxy C23 Ultra'
    assert product_item.description == '256GB, Серый цвет, 200MP камера'
    assert product_item.price == 180000.0
    assert product_item.quantity_in_stock == 5


def test_add_product(product_item):
    assert product_item.


def test_number_of_categories():
    assert Category.number_of_categories == 3


def test_number_of_uniq_goods():
    assert Category.number_of_uniq_goods == 7
