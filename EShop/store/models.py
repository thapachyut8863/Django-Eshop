from django.db import models
from PIL import Image
from .category import Category

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(default='default.jpg', upload_to='products')

    @staticmethod
    def get_all_products():
        return Product.objects.all()