from django.db import models
from product.models import Product, FlavorCategorie, FlavorGroup
from account.models import User
import uuid


class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'cart')

    def get_total_cost(self):
        return sum([item.get_cost() for item in self.items.all()])
    
    def __str__(self):
        return "cart items"+" "+ str(self.customer)+" "+ str(self.id)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE, related_name = 'items', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    flavorgroup= models.ForeignKey(FlavorGroup, on_delete=models.Case, related_name='flavorgrp')
    flavorcategorie = models.ForeignKey(FlavorCategorie, on_delete= models.CASCADE, related_name='flavorctg')
    quantity = models.PositiveIntegerField(null=True, blank=True)
    is_eggless = models.BooleanField()
    message  = models.TextField(null=True, blank=True)
    
    
    def get_cost(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return str(self.cart)





class WishList(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='userWhichlist')

    class Meta:
        ordering = ['-id']


class WishListItem(models.Model):
    wishlist = models.ForeignKey(WishList, on_delete= models.CASCADE,related_name ='items', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)

    class Meta:
        ordering =['-id']
