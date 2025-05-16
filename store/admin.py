from django.contrib import admin
from .models import Product, Category, Collection, Wishlist

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Collection)
admin.site.register(Wishlist)