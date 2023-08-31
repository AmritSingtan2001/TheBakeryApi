from decimal import Decimal
from django.conf import settings
from product.models import Product

class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        

        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity, 'price': str(product.price)}

        elif override_quantity:
            self.cart[product_id]['quantity'] = quantity
            
           
        else:
            qty = int(self.cart[product_id]['quantity'])
            qty2 = qty + int(quantity)
            self.cart[product_id]['quantity'] = str(qty2)
 
        self.save()
    
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    
    def List(self):
        carts = []
        for product_id in self.cart.keys():
            obj = Product.objects.get(id=int(product_id))
            temp_cart = {
                'id': product_id,
                'obj': obj,
                'quantity': int(self.cart[product_id]['quantity']),
                'price': float(int(self.cart[product_id]['quantity']) * float(obj.price))
                
            }
            carts.append(temp_cart)
        return carts
    
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()
    
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()