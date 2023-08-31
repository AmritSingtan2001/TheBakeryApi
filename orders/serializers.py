from rest_framework import serializers
from product.models import Product,FlavorGroup,FlavorCategorie
from account.models import User
from product.serializers import ProductSerializer
from .models import Order, OrderItem,CustomerOrder,ShippingDetails, UserHome,Districts, Coupon
from cart.models import Cart



domain = "http://192.168.18.11:8000"



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ['id','name','email']


class OrderItemSerializer(serializers.ModelSerializer):
    #product = ProductSerializer( read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity','flavorgroup','flavorcategorie','is_eggless','message', 'get_cost']


#district serializer
class DistrictSerializers(serializers.ModelSerializer):
    class Meta:
        model = Districts
        fields = '__all__'


class ShippingDetailsSerializer(serializers.ModelSerializer):
    districts=serializers.SlugRelatedField(
        queryset=Districts.objects.all(), slug_field="district_name"
    )
    class Meta:
        model = ShippingDetails
        fields =['id','fullname','districts','location','landmark','alies','phoneNumber','alternativeNo']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many = True)
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="name"
    )
    shipping_details = ShippingDetailsSerializer()

   
    class Meta:
        model = Order
        fields = ['id', 'user', 'payment_method', 
                            'order_status','itemsPrice',
                            'shippingPrice','taxPrice',
                            'totalPrice', 'get_total_cost',
                            'created', 'updated', 'items',
                            'shipping_details'
                            ]



    def create(self, validated_data):
        items_data = validated_data.pop('items')
        shipping_data = validated_data.pop('shipping_details')
        
        shippingDetails =self.context.get('shippingDetails')

        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        
        user = self.context.get('user')
        try:
            cartId = Cart.objects.get(customer= user)
            cartId.delete()
        except:
            raise serializers.ValidationError({"msg":"no item in cart !"})

        ShippingDetails.objects.create(order=order,
                                        fullname= shippingDetails.fullName,
                                        districts=shippingDetails.district,
                                        location= shippingDetails.location,
                                        landmark= shippingDetails.landMark,
                                        alies= shippingDetails.alies,
                                        phoneNumber = shippingDetails.phoneNo,
                                        alternativeNo= shippingDetails.altPhoneNo
                                        )

        return order
    
class OrderItems(serializers.ModelSerializer):
    product = ProductSerializer( read_only=True)
    flavorgroup = serializers.SlugRelatedField(
        queryset=FlavorGroup.objects.all(), slug_field="flavorName"
    )
    flavorcategorie = serializers.SlugRelatedField(
        queryset=FlavorCategorie.objects.all(), slug_field="flavorCategorieName"
    )

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity','flavorgroup','flavorcategorie' ,'is_eggless','message','get_cost']


class UserOrderSerializer(serializers.ModelSerializer):
    items = OrderItems(many = True)
    user = UserSerializer()

    shipping_details = ShippingDetailsSerializer()

    class Meta:
        model = Order
        fields = ['id', 'user', 'payment_method', 
                            'order_status','itemsPrice',
                            'shippingPrice','taxPrice',
                            'totalPrice', 'get_total_cost',
                            'created', 'updated', 'items',
                            'shipping_details'
                            ]







#customer home 
class  UserHomeSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="name", required=False
    )
    district=serializers.SlugRelatedField(
        queryset=Districts.objects.all(), slug_field="district_name"
    )
    class Meta:
        model= UserHome
        fields =['id','user','fullName','district','location','landMark','alies','phoneNo','altPhoneNo']



# coupon serializer class
class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model =Coupon
        fields ='__all__'





#testing part
class CustomerOrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomerOrder
        fields ='__all__'





