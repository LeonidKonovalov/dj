from django.db import models


class ProductCategories(models.Model):
    """model category"""
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True)
    #is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """model product"""
    name = models.CharField(max_length=128, unique=True)
    image = models.ImageField(upload_to='product_images', blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategories, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} | {self.category}'
