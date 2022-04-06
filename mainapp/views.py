from django.shortcuts import render
from datetime import datetime
import json, os
from mainapp.models import ProductCategories, Product

MODULE_DIR = os.path.dirname(__file__)


def index(request):
    date = datetime.now()
    content = {'title': 'Geekshop', 'date': date}
    return render(request, 'mainapp/index.html', content)


def read_file(name):
    file_path = os.path.join(MODULE_DIR, name)
    return json.load(open(file_path, encoding='utf-8'))


def products(request):
    #cards, categories = read_file('data_products.json')
    year = datetime.now()
    content = {
        'title': 'Geekshop - каталог',
        'categories': ProductCategories.objects.all(),
        'products': Product.objects.all(),
        'year': year,
    }
    return render(request, 'mainapp/products.html', content)


def test(request):
    context = {'title': 'geekshop',
               'header': 'Welcome',
               'user': 'User',
               'products': [
                   {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090'},
                   {'name': 'Синяя куртка The North Face', 'price': '23 725'},
                   {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3  390'},
                   {'name': 'Черный рюкзак Nike Heritage', 'price': '2 590'},
                   {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 390'},
                   {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': '6 390'},
               ],
               'promotion': False,
               'products_promotion': [
                   {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '50'},
                   {'name': 'Синяя куртка The North Face', 'price': '50'},
                   {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '50'},
                   {'name': 'Черный рюкзак Nike Heritage', 'price': '50'},
                   {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '50'},
                   {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': '50'},
               ]}
    return render(request, 'mainapp/test.html', context)
