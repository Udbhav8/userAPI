from django.urls import path
from .views import UserList,UserListUpdate

urlpatterns = [path('users/', UserList.as_view()),
               path('update-user/<int:user_id>', UserListUpdate.as_view()),]