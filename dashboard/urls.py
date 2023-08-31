from django.urls import path
from . import views
app_name ='dashboard'

urlpatterns = [ 
    path('', views.login, name='login'),
    path('logout', views.userlogout, name='logout'),
    path('index', views.index, name='index'),
    path('add/categori', views.addCategories, name='addCategory'),
    path('add/product', views.addProduct, name='addProduct'),
    path('order-list', views.orderList, name='orderList',),
    path('agent-list', views.agentList, name='agentlist'),
    path('user-list', views.userList, name='userlist'),
    path('inbox-email', views.inboxEmail, name='inboxEmail'),
    path('compose-email', views.composeEmail, name='composeEmail'),
    path('email-read', views.readEmail, name='readEmail')
]       