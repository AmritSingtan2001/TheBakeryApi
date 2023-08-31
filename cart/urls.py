from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views
from . views import CartItemViews,CartItemsDeleteUpdate, WhichListAPIView


urlpatterns = [ 
    path('', CartItemViews.as_view()),
    path('delete/<int:id>',CartItemsDeleteUpdate.as_view(), name='cartitemdelete'),
    path('whichlist', WhichListAPIView.as_view(), name='whichList'),
    path('whichlist/<int:id>', WhichListAPIView.as_view(), name='whichList')
]