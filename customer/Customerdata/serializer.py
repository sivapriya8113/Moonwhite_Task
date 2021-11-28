from rest_framework import serializers
from .models import customerdetails,Address
class customerserializer(serializers.ModelSerializer):
    class Meta:
        model = customerdetails
        fields = ['firstname','lastname','email','mobileno']


class addressserializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['customer_id','addr_line1','addr_line2','city','state','pincode']


class requestserilaizer(serializers.Serializer):
      firstname=serializers.CharField()
      lastname=serializers.CharField()
      email=serializers.CharField()
      mobileno=serializers.IntegerField()
      addr_line1 = serializers.CharField()
      addr_line2 = serializers.CharField()
      city = serializers.CharField()
      state = serializers.CharField()
      pincode = serializers.IntegerField()








