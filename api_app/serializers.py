from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .models import Aadhar, Personal, PastExp, Qualification, Address, Bank


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])

        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class AadharSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aadhar
        fields = ['AadharNumber','is_Active']



"""
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'created_date', 'author', 'added_by']

"""