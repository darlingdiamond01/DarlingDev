from rest_framework import viewsets, permissions, filters
from rest_framework.generics import ListAPIView
from .models import Product, Category, Collection, Wishlist
from .serializers import ProductSerializer, CategorySerializer, CollectionSerializer, WishlistSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'brand', 'gender']  # Customize as needed
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at']

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    filterset_fields = ['category__id', 'available', 'color', 'size']
    ordering_fields = ['price', 'name']
    search_fields = ['name', 'description']

class WishlistViewSet(viewsets.ModelViewSet):
    serializer_class = WishlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# === React Frontend View ===
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator

@method_decorator(never_cache, name='dispatch')
class FrontendAppView(TemplateView):
    template_name = 'frontend/index.html'
