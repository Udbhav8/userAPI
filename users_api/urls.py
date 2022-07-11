from django.urls import path
from .views import UserList,UserListUpdate,UserGetOne

urlpatterns = [path('users/', UserList.as_view()),
               path('update-user/<int:user_id>', UserListUpdate.as_view()),
               path('user/<int:user_id>', UserGetOne.as_view())]
