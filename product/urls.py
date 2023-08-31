from django.urls import path,include
from . import views
from . views import (ProductView,
                    ProductDetailsDelete,
                    CategoryView,
                    CategoryRetriveUpdate,
                    CategoryProductList,
                    PopularProduct,
                    FlavorListView
                    )

urlpatterns = [
    path('category', CategoryView.as_view(), name="product_category"),
    path('category/details/<slug:category_slug>', CategoryRetriveUpdate.as_view(), name="product_ctg_details"),
    path('category/related/<slug:category_slug>', CategoryProductList.as_view(), name="product-ctg-product"),
    path('list', ProductView.as_view(), name='productlist' ),
    path('details/<slug:prod_slug>', ProductDetailsDelete.as_view(), name='ProductDetailsDelete' ),
    path('popular-products', PopularProduct.as_view(), name='popular-product'),
    path('flavor',FlavorListView.as_view(), name='flavor')
]