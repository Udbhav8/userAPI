from django.views import View
from django.http import JsonResponse
import json
from .models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class UserList(View):
    def post(self,request):
        data = json.loads(request.body.decode("utf-8"))
        firstName = data.get('firstName')
        lastName = data.get('lastName')
        email = data.get('email')
        number = data.get('number')
        role = data.get('role')
        
        user_data = {
            'firstName': firstName,
            'lastName': lastName,
            'email':email,
            'number':number,
            'role':role,
        }
        
        user = User.objects.create(**user_data)
        
        data = {
            'message':f"New User {user.firstName} {user.lastName} with email:{user.email} created successfully",
        }
        
        return JsonResponse(data,status = 201)
    
    def get(self,request):
        user_count = User.objects.count()
        users = User.objects.all()
        
        user_data = []
        for user in users:
            user_data.append({
                "firstName": user.firstName,
                'lastName': user.lastName,
                "email": user.email,
                "number": user.number,
                "role": user.role,
            })
        data = {
            'users': user_data,
            'count': user_count,
        }
        return JsonResponse(data)
    
 
    
@method_decorator(csrf_exempt, name='dispatch')
class UserListUpdate(View):
    def patch(self,request,user_id):
        data = json.loads(request.body.decode("utf-8"))
        user = User.objects.get(id = user_id)
        user.firstName = data.get('firstName')
        user.lastName = data.get('lastName')
        user.email = data.get('email')
        user.number =   data.get('number')
        user.role = data.get('role')
        user.save()
        
        data = {
            'message':f"User {user.firstName} {user.lastName} with email:{user.email} updated successfully",
        }
        return JsonResponse(data)
    
    def delete(self,request,user_id):
        user = User.objects.get(id = user_id)
        user.delete()
        data = {
            'message':f"User {user.firstName} {user.lastName} with email:{user.email} deleted successfully",
        }
        return JsonResponse(data)