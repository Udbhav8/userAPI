from django.urls import path
from .views import UserList,UserSingle

urlpatterns = [path('users/', UserList.as_view()),
               path('update-user/<int:user_id>', UserSingle.as_view()),]