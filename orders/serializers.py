from rest_framework import serializers
from .models import Order, OrderItem
from store.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'payment_status', 'created_at', 'updated_at', 'items', 'total_price']
        read_only_fields = ['user', 'created_at', 'updated_at']

    def get_total_price(self, obj):
        return sum(item.quantity * item.price for item in obj.items.all())
