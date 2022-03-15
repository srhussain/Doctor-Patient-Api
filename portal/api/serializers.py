from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','line1','pincode','city','state','email','username','is_patient','is_doctor','password','profile']

    def create(self,validated_data):
        user=User.objects.create(email=validated_data['email'],username=validated_data['username'],first_name=validated_data['first_name'],last_name=validated_data['last_name'],line1=validated_data['line1'],city=validated_data['city'],state=validated_data['state'],pincode=validated_data['pincode'],
        profile=validated_data['profile'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()