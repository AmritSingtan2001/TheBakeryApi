from django.contrib import admin

from .models import Order, OrderItem,DeliveryAgent,ShippingDetails,Districts,UserHome,Coupon


class CouponAdmin(admin.ModelAdmin):
    model =Coupon
    list_display = ['id','code','discount','expiration_date','active']
admin.site.register(Coupon, CouponAdmin)


class DistrictsAdmin(admin.ModelAdmin):
    model = Districts
    list_display = ['district_name']
admin.site.register(Districts, DistrictsAdmin)



class OrderItemInline(admin.TabularInline):
    model = OrderItem
   

class ShippingDetailsAdmin(admin.TabularInline):
    model =ShippingDetails


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline,ShippingDetailsAdmin]
    list_filter = ['payment_method', 'order_status']
    
admin.site.register(Order, OrderAdmin)


class DeliveryAgentAdmin(admin.ModelAdmin):
    model = DeliveryAgent
    list_display =['id','name','address','email','phone']
admin.site.register(DeliveryAgent, DeliveryAgentAdmin)

class UserHomeAdmin(admin.ModelAdmin):
    model= UserHome
    list_display = ['user','id','district','location','phoneNo']
admin.site.register(UserHome, UserHomeAdmin)