from django.shortcuts import render,HttpResponse
from product.renderers import UserRenderer
from . models import Product, Category, FlavorCategorie, FlavorGroup
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .serializers import ProductSerializer, ProductCategorySerializer, FlavorCategorie,FlavorGroupSerializer


# category create, update 
class CategoryView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Category.objects.all().order_by('ordering')
    serializer_class = ProductCategorySerializer
    # renderer_classes = [UserRenderer]
    def list(self, request):
        queryset = self.get_queryset()
        serializer = ProductCategorySerializer(queryset, many=True)
        return Response({"data":serializer.data, "success":"true"}, status=status.HTTP_200_OK)


    def post(self, request):
        try:
            serializer = self.serializer_class(data= request.data)
            serializer.is_valid(raise_exception=False)
            serializer.save()
            return Response({"message":"New Product added successfully !","success":"true"},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"Message":"Something wrong!","success":"false"},status= status.HTTP_400_BAD_REQUEST)
        


# category details, update, destory
class CategoryRetriveUpdate(generics.RetrieveAPIView, generics.UpdateAPIView ,generics.DestroyAPIView):
    queryset = Category.objects.all()
    lookup_field = 'category_slug'
    serializer_class =ProductCategorySerializer
    # renderer_classes = [UserRenderer]
    def get(self,  request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            data = serializer.data
            return Response({'data': data,"success":"true"}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"message":"Category not found !","success":"false"}, status=status.HTTP_400_BAD_REQUEST)


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
                return Response("Category not found !", status=status.HTTP_400_BAD_REQUEST)
            self.perform_destroy(instance)
            return Response({"message":"Category Delete Successfully !","success":"true"}, status=status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
            return Response({"message":"Category Not found !","success":"true"})



#produc list and create view section
class ProductView(generics.ListAPIView):
    search_fields = ['product_name',]
    filter_backends = (filters.SearchFilter,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # renderer_classes = [UserRenderer]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ProductSerializer(queryset, many=True)
        # return Response({"data":serializer.data, "success":"true"}, status=status.HTTP_200_OK)
        if len(serializer.data) >=1:
            return Response({"data":serializer.data, "success":"true"}, status=status.HTTP_200_OK)

        else:
            return Response({"data":serializer.data,"message":"We're sorry. We cannot find any matches for your search term.", "success":"true"}, status=status.HTTP_200_OK)
        
    def post(self, request):
        try:
            serializer = self.serializer_class(data= request.data)
            serializer.is_valid(raise_exception=False)
            serializer.save()
            return Response({"message":"New Product added successfully !","success":"true"},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"message":"Something wrong!","success":"false"},status= status.HTTP_400_BAD_REQUEST)
        
    
# product details, update, destory 
class ProductDetailsDelete(generics.RetrieveAPIView,generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = Product.objects.all() 
    lookup_field = 'prod_slug'
    serializer_class = ProductSerializer

    def get(self,  request, *args, **kwargs):
        try:
            instance = self.get_object()
            recommendedProducts = Product.objects.filter(category= instance.category)
            serializer = self.get_serializer(instance)
            data = serializer.data
            recommended_product = self.get_serializer(recommendedProducts, many=True)
            instance.product_views += 1
            instance.save()
            return Response({'data': data,'recommendedProduct':recommended_product.data,"success":"true"}, status=status.HTTP_200_OK)
          
        except Exception as e:
             return Response({"message":"No objects found !","success":"false"}, status=status.HTTP_400_BAD_REQUEST)


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
                return Response("No product found !", status=status.HTTP_400_BAD_REQUEST)
            self.perform_destroy(instance)
            return Response({"message":"Product Delete Successfully !","success":"true"}, status=status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
            return Response({"message":"Product Not found !","success":"true"})


#category realted product list 
class CategoryProductList(generics.ListAPIView, generics.CreateAPIView):
    queryset = Category.objects.all()
    lookup_field = 'category_slug'
    serializer_class =ProductSerializer

    def get(self, request, *args, **kwargs):
        try:
            category  =self.get_object()
            queryset = Product.objects.filter(category =category)
            if len(queryset) >= 1 :
                serializer = ProductSerializer(queryset, many=True)
                return Response({"data":serializer.data, "success":"true"}, status=status.HTTP_200_OK)
            return Response({"message":"Related Product No found !", "success":"false"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message":"not found !", "success":"false"}, status=status.HTTP_400_BAD_REQUEST)

    

# most popular product section
class PopularProduct(generics.ListAPIView):
    queryset = Product.objects.all().order_by('-product_views')[:8]
    serializer_class = ProductSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        return Response({"data":serializer.data, "success":"true"}, status=status.HTTP_200_OK)




class FlavorListView(APIView):
    def get(self, request):
        queryset =  FlavorGroup.objects.all()     #  self.get_queryset()
        serializer = FlavorGroupSerializer(queryset, many=True)
        return Response({ "data": serializer.data}, status=status.HTTP_200_OK)