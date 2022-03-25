from django.shortcuts import render
from datetime import datetime
import json


def index(request):
    date = datetime.now()
    content = {
        'title': 'Geekshop',
        'date': date
    }
    return render(request, 'mainapp/index.html', content)


def products(request):
    with open("mainapp/data_file.json", "r") as read_file:
        cards, categories = json.load(read_file)
        # символы русского языка в json отображаются как \u041c, нечитаемо,
        # сохранил читаемо в json - в html отображаются как спецсимволы
        # общие json или отдельно?
    '''cards = [
        {'name': 'Худи черного цвета с монограммами adidas Originals',
         'price': '6 090,00 руб.',
         'desc': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
         'img': 'vendor/img/products/Adidas-hoodie.png'
         },
        {'name': 'Синяя куртка The North Face',
         'price': '23 725,00 руб.',
         'desc': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
         'img': 'vendor/img/products/Blue-jacket-The-North-Face.png'
         },
        {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
         'price': '3 390,00 руб.',
         'desc': 'Материал с плюшевой текстурой. Удобный и мягкий.',
         'img': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'
         },
        {'name': 'Черный рюкзак Nike Heritage',
         'price': '2 340,00 руб.',
         'desc': 'Плотная ткань. Легкий материал.',
         'img': 'vendor/img/products/Black-Nike-Heritage-backpack.png'
         },
        {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
         'price': '13 590,00 руб.',
         'desc': 'Гладкий кожаный верх. Натуральный материал.',
         'img': 'vendor/img/products/Black-Dr-Martens-shoes.png'
         },
        {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
         'price': '2 890,00 руб.',
         'desc': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
         'img': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'
         },

    ]'''
    '''categories = [
        {'name': 'Новинки'},
        {'name': 'Одежда'},
        {'name': 'Обувь'},
        {'name': 'Аксесуары'},
        {'name': 'Подарки'},
    ]'''
    year = datetime.now()
    content = {
        'title': 'Geekshop - каталог',
        'categories': categories,
        'cards': cards,
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
