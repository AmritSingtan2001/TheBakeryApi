from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from account.models import User
from product.models import Product, FlavorGroup,FlavorCategorie
import uuid
import random


phone_validator = RegexValidator(
    r'\d{3}?-?\d{3}?-?\d{4}', 'Only ten numbers and dashes allowed.')


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.FloatField()
    expiration_date = models.DateTimeField()
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id',]

    def __str__(self):
        return str(self.code)



class DeliveryAgent(models.Model):
    name= models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    


class Order(models.Model):
    PAYMENT_CHOICES = [('credit', 'Credit'),('cod', 'Cash on Delivery')]

    ORDER_STATUS_CHOICES = [('pending', 'Pending'),
                            ('accept','Accept'),
                            ('on_delivery', 'On Delivery'), 
                            ('delivered', 'Delivered')
                            ]

    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'orders')
    payment_method = models.CharField(max_length = 50, choices = PAYMENT_CHOICES)
    order_status = models.CharField(max_length = 50, choices = ORDER_STATUS_CHOICES, default="pending")
    itemsPrice= models.FloatField(null=True, blank=True)
    shippingPrice = models.FloatField(null=True, blank=True)
    taxPrice = models.FloatField(null=True, blank=True)
    totalPrice = models.FloatField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    agent = models.OneToOneField(DeliveryAgent, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return f"Order {self.id} - {self.user}"
    
    def get_total_cost(self):
        return sum([item.get_cost() for item in self.items.all()])

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE, related_name = 'items',  null=True, blank=True)
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name="productdetails")
    quantity = models.PositiveIntegerField(default = 1)
    flavorgroup= models.ForeignKey(FlavorGroup, on_delete=models.Case, related_name='flavor')
    flavorcategorie = models.ForeignKey(FlavorCategorie, on_delete= models.CASCADE, related_name='flavorCategorie')
    is_eggless = models.BooleanField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    ordered_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.id}"
    
    def get_cost(self):
        return self.product.price * self.quantity
    
    class Meta:
        ordering = ('-ordered_date',)


class Districts(models.Model):
    district_name = models.CharField(max_length=150)

    def __str__(self):
        return self.district_name


class ShippingDetails(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True, related_name='shipping_details')
    fullname = models.CharField(max_length=150, null=True, blank=True,)
    districts =models.ForeignKey(Districts, on_delete=models.CASCADE, related_name='district', null=True, blank=True)
    location= models.CharField(max_length=150,null=True, blank=True,)
    landmark= models.CharField(max_length=150, null=True, blank=True,)
    alies= models.CharField(max_length=150, null=True, blank=True,)
    phoneNumber = models.CharField(max_length=150, null=True, blank=True,)
    alternativeNo= models.CharField(max_length=150, null=True, blank=True,)
    


    def __str__(self):
        return f"Shipping Details for Order {self.order.id}"







class CustomerOrder(models.Model):
    PAYMENT_CHOICES = [('credit', 'Credit'),('cod', 'Cash on Delivery')]

    ORDER_STATUS_CHOICES = [('unverified', 'Unverified'),
                            ('verified','Verified'),
                            ('on_delivery', 'On Delivery'), 
                            ('delivered', 'Delivered')
                            ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    quantity = models.IntegerField()
    payment_method = models.CharField(max_length = 50, choices = PAYMENT_CHOICES)
    order_status = models.CharField(max_length = 50, choices = ORDER_STATUS_CHOICES)
    orderAt= models.DateTimeField(auto_now=True)
    updatedAt= models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} "
    
    def get_cost(self):
        return self.product.price * self.quantity


    def get_total_cost(self):
        return sum([item.get_cost() for item in self.items.all()])
    
    
    class Meta:
        ordering = ('-orderAt',)



class UserHome(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='userhome', null=True, blank=True)
    fullName = models.CharField(max_length=150)
    district =models.ForeignKey(Districts, on_delete=models.CASCADE, related_name='districts', null=True, blank=True)
    location= models.CharField(max_length=150)
    landMark= models.CharField(max_length=150)
    alies= models.CharField(max_length=150)
    phoneNo = models.CharField(max_length=150)
    altPhoneNo= models.CharField(max_length=150)


    class Meta:
        ordering = ['-id',]

    def __str__(self):
        return str(self.user) +self.fullName