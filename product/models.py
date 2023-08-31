from django.db import models
from autoslug import AutoSlugField
from django.core.validators import MaxValueValidator, MinValueValidator



class FlavorGroup(models.Model):
    flavorName = models.CharField(max_length=150)


    class Meta:
        ordering =['id',]

    def __str__(self):
        return self.flavorName
    

class FlavorCategorie(models.Model):
    flavor = models.ForeignKey(FlavorGroup, on_delete=models.CASCADE, related_name='items')
    flavorCategorieName = models.CharField(max_length=150)
    price = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ['id',]

    def __str__(self):
        return self.flavorCategorieName



class Category(models.Model):
    category_name = models.CharField(max_length=150)
    image1 = models.ImageField(upload_to='cakecategoryimage/')
    image2 = models.ImageField(upload_to='cakecategoryimage/')
    category_slug = AutoSlugField(populate_from='category_name', unique=True, default=None)
    ordering =models.PositiveIntegerField()

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_ctg')
    product_name = models.CharField(max_length=150)
    product_image= models.ImageField(upload_to='productimage/', null=True, blank=True)
    price = models.PositiveIntegerField()
    description= models.TextField()
    product_views =models.PositiveIntegerField(default=1)
    created_date = models.DateField(auto_now=True)
    updated_date = models.DateField(auto_now=True)
    prod_slug = AutoSlugField(populate_from = 'product_name', unique=True, default=None)
    isInstock = models.PositiveIntegerField()
    rating = models.PositiveIntegerField( validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])

    class Meta:
        ordering =['-id',]
    
    def __str__(self):
        return self.product_name
