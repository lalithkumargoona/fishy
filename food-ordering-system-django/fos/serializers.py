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
