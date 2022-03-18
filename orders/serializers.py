from rest_framework import serializers
from orders.models import Order
from users.serializers import UserSerializer


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    customer = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Order
        fields = ['url', 'dish_name', 'description', 'datetime_ordered', 'datetime_fulfilled', 'customer']