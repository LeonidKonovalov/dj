from mainapp.models import ProductCategories

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "geekshop.settings")
django.setup()
category = ProductCategories(name='Одежда', descriptions='Вся одежда')
category = ProductCategories(name='Одежда', description='Вся одежда')
category.save()
category = ProductCategories.objects.create(name='Обувь', description='Вся обувь')
print(category)
print(ProductCategories.objects.get())
#python manage.py dumpdata mainapp.products > mainapp/fixtures/product.json