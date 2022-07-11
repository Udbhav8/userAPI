from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list = ('firstName','lastName', 'email', 'number', 'role')
    
admin.site.register(User, UserAdmin)