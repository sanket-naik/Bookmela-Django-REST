from rest_framework.routers import DefaultRouter
from .api import *

router=DefaultRouter()
router.register(r'Users',UsersViewSet)
router.register(r'Books',BooksViewSet) 

urlpatterns=router.urls