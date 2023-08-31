from django.urls import path, include

from rest_framework.routers import SimpleRouter
from . import views
from .views import (
                    PlaceOrder,
                    OrderDeleteUpdateView,
                    OrderShippingDetails,
                    OrderCreateView,
                    OrderDeleteUpdateView,
                    UserHomeAPIView,
                    DistrictAPIView,
                    CouponeAPIView
                    )




urlpatterns = [ 
    path('', OrderCreateView.as_view(), name="orderlist"),
    # path('', OrderListView.as_view(), name="orderlist"),
    path('single/order/<int:id>', OrderDeleteUpdateView.as_view(), name="orderdelet"),
    path('place-order', PlaceOrder.as_view(), name = 'place_order'),
    # path('shipping-details', OrderShippingDetails.as_view(), name='shippindetails'),
    path('district', DistrictAPIView.as_view(), name="district"),
    path('user/home', UserHomeAPIView.as_view(), name='userHome'),
    path('coupone', CouponeAPIView.as_view(), name='coupone'),
]