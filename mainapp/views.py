from django.shortcuts import render
from datetime import datetime
import json, os
from mainapp.models import ProductCategories, Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import DetailView

MODULE_DIR = os.path.dirname(__file__)


def index(request):
    date = datetime.now()
    content = {'title': 'Geekshop', 'date': date}
    return render(request, 'mainapp/index.html', content)


def read_file(name):
    file_path = os.path.join(MODULE_DIR, name)
    return json.load(open(file_path, encoding='utf-8'))


# #def products(request):
#     #cards, categories = read_file('data_products.json')
#     year = datetime.now()
#     content = {
#         'title': 'Geekshop - каталог',
#         'categories': ProductCategories.objects.all(),
#         'products': Product.objects.all(),
#         'year': year,
#     }
#     return render(request, 'mainapp/products.html', content)

def products(request,id_category=None,page=1):

    if id_category:
        products_ = Product.objects.filter(category_id=id_category)
    else:
        products_ = Product.objects.all()

    pagination = Paginator(products_,per_page=3)

    try:
        product_pagination = pagination.page(page)
    except PageNotAnInteger:
        product_pagination = pagination.page(1)
    except EmptyPage:
        product_pagination = pagination.page(pagination.num_pages)
    content = {
        'title' : 'Geekshop - Каталог',
        'categories': ProductCategories.objects.all(),
        'products': product_pagination

    }


    return  render(request,'mainapp/products.html',content)


#

class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'

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
