from .models import Cart, CartItem, WishListItem, WishList
from rest_framework import serializers
from product.serializers import ProductSerializer, FlavorGroupSerializer,FlavorCategorieSerializer
from account.models import User
from product.models import Product, FlavorCategorie,FlavorGroup
# from cart import Cart


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id','cart','product','quantity','flavorgroup','flavorcategorie','message','is_eggless']




class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many = True)
    customer = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="name"
    )

    class Meta:
        model = Cart
        fields = ['id', 'customer', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = self.context.get('user')
        cart= Cart.objects.filter(customer = user).first()
        if cart is None:
            cart = Cart.objects.create(**validated_data)
        else:
            cart = Cart.objects.filter(customer = user).first()
            cartitems = cart.items.all()
            cartitems.delete()

        for item_data in items_data:
            CartItem.objects.create(cart=cart, **item_data)

        return cart



# cart item views section
class CartItems_Serializer(serializers.ModelSerializer):
    product= ProductSerializer()
    class Meta:
        model = CartItem
        fields = ['id','cart','product','flavorgroup','flavorcategorie','quantity','message','is_eggless']


class CartItemListSerializer(serializers.ModelSerializer):
    items = CartItems_Serializer(many = True, read_only = True)
    customer = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="name"
    )
    class Meta:
        model = Cart
        fields = ['id', 'customer', 'items']

    




# wish add serializer
class WishListItemSerializer(serializers.ModelSerializer):
    # product= ProductSerializer()
    class Meta:
        model= WishListItem
        fields= ['wishlist','product']


class WishListSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="name"
    )
    items = WishListItemSerializer(many = True)

    class Meta:
        model = WishList
        fields = ['id','user','items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = self.context.get('user')
        WishListID= WishList.objects.filter(user = user).first()
        if WishListID is None:
            WishListID = WishList.objects.create(**validated_data)
        else:
            WishListID = WishList.objects.filter(user = user).first()
            wishlistitem = WishListID.items.all()
            wishlistitem.delete()

        for item_data in items_data:
            WishListItem.objects.create(wishlist=WishListID, **item_data)

        return WishListID


#wishList view
class WishListViewItemSerializer(serializers.ModelSerializer):
    product= ProductSerializer()
    class Meta:
        model= WishListItem
        fields= ['wishlist','product']

class WishListViewSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="name"
    )
    items = WishListViewItemSerializer(many = True)

    class Meta:
        model = WishList
        fields = ['id','user','items']
