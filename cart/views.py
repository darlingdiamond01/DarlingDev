from django.urls import path
from .views import CartViewSet

cart_list = CartViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'delete'})

urlpatterns = [
    path('', cart_list, name='cart'),
    path('api/cart/', include('cart.urls')),
]
