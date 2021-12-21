from django.db import models
from category.models import Category

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'media/photoes/products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name