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
    # given
    category = Category("test_category", "test_desc", [])
    category.add_product(Product("test_name", "test_desc", 10, 3))
    # then
    assert category.products == '\nКатегория: test_category\ntest_name, 10 руб. Остаток: 3 шт.\n'
