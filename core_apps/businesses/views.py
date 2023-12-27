from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .models import Business,Product
from .serializers import BusinessSerializer,ProductSerializer
from rest_framework.exceptions import ValidationError


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'  # This indicates the lookup parameter (primary key by default)

#==================================================================================
    

class BusinessListCreateAPIView(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BusinessDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = [IsAuthenticated]
    

    def get_object(self):
        business_id = self.kwargs.get('pk')  # Assuming the URL pattern captures the 'pk' parameter
        return get_object_or_404(self.queryset, pkid=business_id)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class AddProductToBusinessAPIView(generics.UpdateAPIView):
    serializer_class = BusinessSerializer
    queryset = Business.objects.all()

    def update(self, request, *args, **kwargs):
        business_id = kwargs.get('pk')
        product_id = request.data.get('product_id')

        try:
            business = self.get_object()
            product = Product.objects.get(pkid=product_id)
            business.projects.add(product)
            serializer = self.get_serializer(business)
            return Response(serializer.data)
        except Business.DoesNotExist:
            return Response({'error': 'Business not found'}, status=status.HTTP_404_NOT_FOUND)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)