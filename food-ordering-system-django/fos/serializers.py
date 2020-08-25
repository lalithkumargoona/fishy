from .models import *
from rest_framework import serializers


class CustomerSignupSerializer(serializers.Serializer):
    cust_name = serializers.CharField(max_length=50, min_length=1, required=True)
    cust_phone = serializers.CharField(max_length=14, min_length=1, required=True)
    cust_email = serializers.CharField(max_length=50, min_length=1, required=True)


class SendOTPSerializer(serializers.Serializer):

    cust_phone = serializers.CharField(max_length=14, min_length=1, required=True)
    cust_req_type = serializers.CharField(max_length=13, min_length=1, required=True)


class OtpSerializer(serializers.Serializer):
    cust_phone = serializers.CharField(max_length=14, min_length=1, required=True)
    cust_otp = serializers.CharField(max_length=4, min_length=1, required=True)
    cust_req_type = serializers.CharField(max_length=13, min_length=1, required=True)
    cust_device_id = serializers.CharField(max_length=256, min_length=1, required=True)


class CustomerDataSerializer(serializers.ModelSerializer):

    cust_phone = serializers.CharField(source='cust_phone')
    cust_name = serializers.CharField(source='cust_name')
    email = serializers.EmailField(source='cust_email')
    device_id = serializers.CharField(source='cust_deviceid')

    class Meta:
        model = CustomerDetails
        fields = ('phone', 'name', 'email', 'device_id')


class AddFoodCategorySerializer(serializers.Serializer):

    category_name = serializers.CharField(max_length=140, min_length=1, required=True)


class UpdateFoodToOrderSerializer(serializers.Serializer):

    order_id = serializers.CharField(max_length=140, min_length=1, required=True)
    food_id = serializers.CharField(max_length=140, min_length=1, required=True)
    food_qty = serializers.CharField(max_length=140, min_length=1, required=True)


class RemoveFoodToOrderSerializer(serializers.Serializer):

    order_id = serializers.CharField(max_length=140, min_length=1, required=True)
    food_id = serializers.CharField(max_length=140, min_length=1, required=True)


class DeleteOrderSerializer(serializers.Serializer):

    order_id = serializers.CharField(max_length=140, min_length=1, required=True)
    food_id = serializers.CharField(max_length=140, min_length=1, required=True)
    food_qty = serializers.CharField(max_length=140, min_length=1, required=True)


class CustomerDetailsSerializer(serializers.Serializer):

    phone = serializers.CharField(max_length=140, min_length=1, required=True)
    name = serializers.CharField(max_length=140, min_length=1, required=True)
    email = serializers.CharField(max_length=140, min_length=1, required=True)


class CreateOrderIdSerializer(serializers.Serializer):

    cust_id = serializers.CharField(max_length=140, min_length=1, required=True)


class OrderIdSerializer(serializers.Serializer):

    order_id = serializers.CharField(max_length=140, min_length=1, required=True)


class CheckoutSerializer(serializers.Serializer):

    order_id = serializers.CharField(max_length=140, min_length=1, required=True)


class ViewSalesTodaySerializer(serializers.Serializer):

    order_status = serializers.CharField(max_length=140, min_length=1, required=True)


class AddFoodDetailsSerializer(serializers.Serializer):

    category_id = serializers.CharField(max_length=140, min_length=1, required=True)
    name = serializers.CharField(max_length=140, min_length=1, required=True)
    customer_price = serializers.CharField(max_length=8, min_length=1, required=True)
    dealer_price = serializers.CharField(max_length=8, min_length=1, required=True)
    offer_price = serializers.CharField(max_length=8, min_length=1, required=True)
    description = serializers.CharField(max_length=1024, min_length=1, required=True)
    image = serializers.CharField(max_length=1000, min_length=1, required=True)
    gross_weight = serializers.CharField(max_length=5, min_length=1, required=True)
    net_weight = serializers.CharField(max_length=5, min_length=1, required=True)


class AddDeliveryPersonSerializer(serializers.Serializer):

    delivery_person_name = serializers.CharField(max_length=140, min_length=1, required=True)
    delivery_person_phone = serializers.CharField(max_length=140, min_length=1, required=True)


class AssignDeliverPersonToDeliverOrderSerializer(serializers.Serializer):

    order_id = serializers.CharField(max_length=140, min_length=1, required=True)
    delivery_person_id = serializers.CharField(max_length=140, min_length=1, required=True)


class UpdateOrderSerializer(serializers.Serializer):

    order_id = serializers.CharField(max_length=140, min_length=1, required=True)
    order_status = serializers.CharField(max_length=140, min_length=1, required=True)
