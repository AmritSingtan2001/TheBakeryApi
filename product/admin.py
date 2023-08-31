from django.contrib import admin
from . models import Category, Product, FlavorGroup, FlavorCategorie


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display =['category_name','image1','image2']
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['product_name','price','product_image']
admin.site.register(Product,ProductAdmin)


class FlavorCategorieAdmin(admin.TabularInline):
    model =FlavorCategorie

class FlavorGroupAdmin(admin.ModelAdmin):
    inlines =[FlavorCategorieAdmin]
    list_display =['flavorName']
admin.site.register(FlavorGroup,FlavorGroupAdmin)