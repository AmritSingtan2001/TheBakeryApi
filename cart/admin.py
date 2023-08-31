from django.contrib import admin
from .models import Cart, CartItem, WishListItem, WishList


class CartItemsAdmin(admin.TabularInline):
    model = CartItem

class CartAdmin(admin.ModelAdmin):
    inlines =[CartItemsAdmin]
    list_display = ['customer','id']
admin.site.register(Cart,CartAdmin)


# class WishListItemAdmin(admin.ModelAdmin):
#     model = WishListItem
#     list_display=['user','product','id']
# admin.site.register(WishListItem,WishListItemAdmin)

class WishListItemAdmin(admin.TabularInline):
    model  = WishListItem

class WishListAdmin(admin.ModelAdmin):
    inlines = [WishListItemAdmin]
    list_display = ['user']
admin.site.register(WishList, WishListAdmin)