from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    final_price = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['product', 'qty', 'discount', 'final_price']
        extra_kwargs = {
            'order': {'read_only': True}
        }

    def get_final_price(self, obj):
        return obj.get_final_price()


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, write_only=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'date', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            product = item_data['product']
            qty = item_data['qty']

            # Stock validation
            if product.in_stock < qty:
                raise serializers.ValidationError(f"Not enough stock for product: {product.name}")

            # Reduce stock
            product.in_stock -= qty
            product.save()

            # Create order item
            OrderItem.objects.create(order=order, **item_data)

        return order

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', None)

        # Update basic order fields
        instance.customer = validated_data.get('customer', instance.customer)
        instance.save()

        if items_data is not None:
            # Restore stock from existing items
            for item in instance.orderitem_set.all():
                product = item.product
                product.in_stock += item.qty
                product.save()

            # Delete old items
            instance.orderitem_set.all().delete()

            # Add new items
            for item_data in items_data:
                product = item_data['product']
                qty = item_data['qty']

                if product.in_stock < qty:
                    raise serializers.ValidationError(f"Not enough stock for product: {product.name}")

                product.in_stock -= qty
                product.save()

                OrderItem.objects.create(order=instance, **item_data)

        return instance
