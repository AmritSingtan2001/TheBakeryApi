from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Cart,CartItem, WishListItem, WishList
from .serializers import CartSerializer,CartItemListSerializer,WishListItemSerializer,WishListViewSerializer,WishListSerializer,CartItems_Serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

class CartItemViews(APIView):

    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user= self.request.user
        if user.is_staff:
            return Cart.objects.all()
        else:
            return Cart.objects.filter(customer=user)


    def get(self, request):
        queryset =  self.get_queryset()     # Cart.objects.all()
        serializer = CartItemListSerializer(queryset, many=True)
        return Response({ "data": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CartSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Item added Successfully !", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




class CartItemsDeleteUpdate(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = CartSerializer
    permission_classes=[IsAuthenticated]
    def destroy(self, request, *args, **kwargs):
        try:
            cartID = Cart.objects.get(customer=request.user)
            cartID.delete()
            # cart_item_id = self.kwargs['id']
            # cart_item = get_object_or_404(CartItem, cart=cartID, id=cart_item_id)
            # cart_item.delete()
            return Response({"message": "Cart Deleted Successfully!", "success": "true"}, status=status.HTTP_200_OK)

        except CartItem.DoesNotExist:
            return Response({"message": "Cart item not found!", "success": "false"}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"message": "Cart  not found !", "success": "false"}, status=status.HTTP_400_BAD_REQUEST)
    



class WhichListAPIView(generics.DestroyAPIView, generics.RetrieveAPIView, generics.CreateAPIView):
    lookup_field ='id'
    serializer_class = WishListSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        user= self.request.user
        if user.is_staff:
            return WishList.objects.all()
        else:
            return WishList.objects.get(user = user)

    def get(self,  request, *args, **kwargs):
        try:
            instance = self.get_queryset()
            serializer =WishListViewSerializer(instance)
            data = serializer.data
            
            return Response({'data': data,"success":"true"}, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({"message":"Sorry ! something wrong.","success":"false"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = WishListSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Item added Successfully !", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    

