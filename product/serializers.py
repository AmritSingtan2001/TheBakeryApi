from . models import Product, Category, FlavorGroup, FlavorCategorie
from rest_framework import serializers


domain = "http://192.168.18.11:8000"

class ProductCategorySerializer(serializers.ModelSerializer):
    image1 = serializers.SerializerMethodField('get_image_url')
    image2 = serializers.SerializerMethodField('get_image2_url')
    class Meta:
        model = Category
        fields =['category_name','image1','image2','category_slug','ordering']


    def get_image_url(self, obj):
        return f'{domain}{obj.image1.url}'
    
    def get_image2_url(self, obj):
        return f'{domain}{obj.image2.url}'
    

class RecommendedProductSerializer(serializers.ModelSerializer):
    pass

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field="category_name"
    )

    product_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Product
        fields = ('id','category','product_name','product_image','product_url','price','description','product_views','prod_slug','isInstock','rating')

    def get_image_url(self, obj):
        return f'{domain}{obj.product_image.url}'
    

#flavor 
class FlavorCategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlavorCategorie
        fields ='__all__'

class FlavorGroupSerializer(serializers.ModelSerializer):
    items = FlavorCategorieSerializer(many = True)

    class Meta:
        model = FlavorGroup
        fields =['id','flavorName','items']
