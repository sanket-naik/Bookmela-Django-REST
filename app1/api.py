from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *

class UsersViewSet(ModelViewSet):
	queryset=Users.objects.all()
	serializer_class=UsersSerializer

class BooksViewSet(ModelViewSet):
	queryset=Books.objects.all()
	serializer_class=BooksSerializer