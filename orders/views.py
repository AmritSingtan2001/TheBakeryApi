from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from account.models import User
from .models import Order, OrderItem,CustomerOrder,ShippingDetails,UserHome,Districts,Coupon
from .serializers import ( OrderSerializer, 
                        OrderItemSerializer,
                        CustomerOrderSerializer,
                        ShippingDetailsSerializer,
                        OrderItems,
                        UserOrderSerializer,
                        UserHomeSerializer,
                        DistrictSerializers,
                        CouponSerializer
                        
                        )
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
import json
from rest_framework.views import APIView


class OrderCreateView(APIView):
   
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user= self.request.user
        if user.is_staff:
            return Order.objects.all()
        else:
            return Order.objects.filter(user=user)

    def get(self, request):
        queryset =  self.get_queryset()   # Order.objects.all() 
        serializer = UserOrderSerializer(queryset, many=True)
        return Response({"data":serializer.data, "success":"true"}, status=status.HTTP_200_OK)
    
    def post(self, request):
        shippingID=request.data.get('shipping_details')
        shippingId=shippingID.get('id')
        shippingDetails = UserHome.objects.get(id= shippingId)
        serializer = OrderSerializer(data=request.data,context={'user': request.user,'shippingDetails':shippingDetails})
        

        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Order Place successfully !","data":serializer.data, "success":"true"}, status=status.HTTP_201_CREATED)
        return Response({"message":serializer.errors, "success":"false"}, status=status.HTTP_400_BAD_REQUEST)





#userrelated order list

class OrderList(generics.ListAPIView):
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user= self.request.user
        print(user)
        if user.is_staff:
            return Order.objects.all()
        else:
            return Order.objects.filter(user=user)




#Order Detail View

class OrderDeleteUpdateView(generics.DestroyAPIView, generics.UpdateAPIView, generics.RetrieveAPIView):
    # queryset = Order.objects.all()
    lookup_field = 'id'
    serializer_class = UserOrderSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user= self.request.user
        print(user)
        if user.is_staff:
            return OrderItem.objects.all()
        else:
            # uerdata= User.object.get()
            return Order.objects.filter(user=user)
        
    def get(self,  request, *args, **kwargs):
        try:
            print(self.get_object())
            instance = self.get_object()
            email= self.request.user.email
            serializer = self.get_serializer(instance)
            data = serializer.data
            
            return Response({'data': data,"success":"true"}, status=status.HTTP_200_OK)
    
        except Exception as e:
            print(e)
            return Response({"message":"Order not found !","success":"false"}, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Updated successfully","success":"true"}, status= status.HTTP_200_OK)

            else:
                return Response({"message": "Update fail !", "details": serializer.errors, "success":"false"},status= status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"message":"Update Faill !","success":"false"},status= status.HTTP_400_BAD_REQUEST)



    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            if instance is None:
                return Response("Order not found !", status=status.HTTP_400_BAD_REQUEST)
            self.perform_destroy(instance)
            return Response({"message":"Order Delete Successfully !","success":"true"}, status=status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
            return Response({"message":"Order Not found !","success":"true"})


class PlaceOrder(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    def get_queryset(self):
        user= self.request.user
        if user.is_staff:
            return OrderItem.objects.all()
        else:
            return OrderItem.objects.filter(user=user)


#district
class DistrictAPIView(generics.RetrieveAPIView):
    serializer_class = DistrictSerializers
    
    def get_queryset(self):
        return Districts.objects.all()
    
    def get(self,  request, *args, **kwargs):
        instance =  self.get_queryset() 
        serializer = self.get_serializer(instance, many=True)
        return Response({'data': serializer.data,"success":"true"}, status=status.HTTP_200_OK)


#user home 
class UserHomeAPIView( generics.CreateAPIView, generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = UserHomeSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user= self.request.user
        if user.is_staff:
            return UserHome.objects.all()
        else:
            return UserHome.objects.filter(user=user)
        
    def get(self,  request, *args, **kwargs):
        try:
            instance =  self.get_queryset() 
            serializer = self.get_serializer(instance,context={'user':request.user}, many=True)
            data = serializer.data
            
            return Response({'data': data,"success":"true"}, status=status.HTTP_200_OK)
    
        except Exception as e:
            print(e)
            return Response({"message":"user data not found !","success":"false"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Shipping details save successfully !","data":serializer.data, "success":"true"}, status=status.HTTP_201_CREATED)
        return Response({"message":serializer.errors, "success":"false"}, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Updated successfully","success":"true"}, status= status.HTTP_200_OK)

            else:
                return Response({"message": "Update fail !", "details": serializer.errors, "success":"false"},status= status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"message":"Update Faill !","success":"false"},status= status.HTTP_400_BAD_REQUEST)



#coupone
class CouponeAPIView(generics.ListAPIView):
    serializer_class = CouponSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Coupon.objects.all()
        else:
            return Coupon.objects.filter(active=True).first()
        
    def get(self,  request, *args, **kwargs):
        try:
            instance =  self.get_queryset()
            serializer = self.get_serializer(instance)
            data = serializer.data
            
            return Response({'data': data,"success":"true"}, status=status.HTTP_200_OK)
    
        except Exception as e:
            print(e)
            return Response({"message":"you need to login first !","success":"false"}, status=status.HTTP_400_BAD_REQUEST)





class OrderShippingDetails(generics.CreateAPIView):
    # permission_classes=[IsAuthenticated]
    queryset = ShippingDetails.objects.all()
    serializer_class = ShippingDetailsSerializer
    # def get_queryset(self):
    #     user= self.request.user
    #     if user.is_staff:
    #         return OrderItem.objects.all()
    #     else:
    #         return OrderItem.objects.filter(user=user)



