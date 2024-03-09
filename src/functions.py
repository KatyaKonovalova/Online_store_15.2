import os
import json


def get_inf():
    with open(os.path.join('../src/products.json'), encoding='utf8') as file:
        goods_inf = json.load(file)
        return goods_inf
