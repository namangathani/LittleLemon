#define Serializer class for User model
from django.contrib.auth.models import User
from rest_framework import serializers

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']