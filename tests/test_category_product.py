import pytest
from src.category_product import Category
from src.category_product import Product


@pytest.fixture
def category_items():
    return Category('Смартфоны', 'Смартфоны, как средство не только коммуникации, '
                                 'но и получение дополнительных функций для удобства жизни',
                    ['Samsung Galaxy C23 Ultra', 'Iphone 15', 'Xiaomi Redmi Note 11'])


@pytest.fixture
def product_items():
    return Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)


def test_init_category(category_items):

    assert category_items.name == 'Смартфоны'
    assert category_items.descriptions == ('Смартфоны, как средство не только коммуникации, но и получение '
                                           'дополнительных функций для удобства жизни')
    assert category_items.goods == ['Samsung Galaxy C23 Ultra', 'Iphone 15', 'Xiaomi Redmi Note 11']


def test_init_product(product_items):

    assert product_items.name == 'Samsung Galaxy C23 Ultra'
    assert product_items.description == '256GB, Серый цвет, 200MP камера'
    assert product_items.price == 180000.0
    assert product_items.quantity_in_stock == 5


def test_number_of_categories():
    assert Category.number_of_categories == 3


def test_number_of_uniq_goods():
    assert Category.number_of_uniq_goods == 7

def givenEmptyCatalog_whenAddProduct_thenProductIsAdded():
    # given
    catalog = Category("testCategoty", "test", [])
    # when
    catalog.add_product(Product("testName", "testDesc", 0, 0))
    # then
    # check than catolog contains product with expeted fields

def test_givenCatalogWithExistingProduct_whenUpdateProduct_thenProductInCatalogHasMaxCostAndSumQuantity():

    # given
    category = Category("testCategoty", "test", [])
    category.add_product(Product("testName", "testDesc", 10, 3))
    # when
    category.add_product(Product("testName", "testDesc", 20, 4))
    # then
    product_in_catalog = category.get_product_by_name('testName')
    assert product_in_catalog.price == 20
    assert product_in_catalog.quantity_in_stock == 7

def


