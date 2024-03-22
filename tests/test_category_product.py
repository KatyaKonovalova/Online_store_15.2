import pytest

from src.category_product import Category
from src.category_product import Product
from src.category_product import Smartphone


@pytest.fixture
def category_item():
    return Category('Смартфоны', 'Смартфоны, как средство не только коммуникации, '
                                 'но и получение дополнительных функций для удобства жизни')


@pytest.fixture
def product_item():
    return Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)


def test_init_category(category_item):
    assert category_item.name == 'Смартфоны'
    assert category_item.description == ('Смартфоны, как средство не только коммуникации, но и получение '
                                         'дополнительных функций для удобства жизни')


def test_init_product(product_item):
    assert product_item.name == 'Samsung Galaxy C23 Ultra'
    assert product_item.description == '256GB, Серый цвет, 200MP камера'
    assert product_item.price == 180000.0
    assert product_item.quantity_in_stock == 5


def test_number_of_categories():
    assert Category.number_of_categories == 3


def test_number_of_uniq_goods():
    assert Category.number_of_uniq_goods == 7


def test_add_product():
    """givenCategoryWithExistingProduct_whenUpdateProduct_thenProductInCatalogHasMaxCostAndSumQuantity"""
    # given
    category = Category("test_category", "test_desc", [])
    category.add_product(Product("test_name", "test_desc", 10, 3))
    # when
    category.add_product(Product("test_name", "test_desc", 20, 4))
    # then
    product_in_catalog = category.get_product_by_name('test_name')
    assert product_in_catalog.price == 20
    assert product_in_catalog.quantity_in_stock == 7


def test_products():

    category = Category("test_category", "test_desc", [])
    category.add_product(Product("test_name", "test_desc", 10, 3))

    assert category.products == '\nКатегория: test_category\ntest_name, 10 руб. Остаток: 3 шт.\n'


def test_add_different_classes():
    smartphone = Smartphone('test_category_s', 'test_desc_s', 1, 2, 1.3, 'test_model_s', 4, 'test_color_s')
    product = Product("test_name", "test_desc", 5, 6)
    with pytest.raises(ValueError):
        smartphone + product


def test_add_same_classes():
    smartphone = Smartphone('test_category_s', 'test_desc_s', 1, 2, 1.3, 'test_model_s', 4, 'test_color_s')
    product = Product("test_name", "test_desc", 5, 6)
    assert smartphone.price * smartphone.quantity_in_stock + product.price * product.quantity_in_stock == 32

