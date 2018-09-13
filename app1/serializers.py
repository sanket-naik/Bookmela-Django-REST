from rest_framework import serializers

from .models import *


class UsersSerializer(serializers.ModelSerializer):

	class Meta:
		model=Users
		fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):
	users=UsersSerializer(read_only=True, many=True)

	class Meta:
		model=Books
		fields = '__all__'

