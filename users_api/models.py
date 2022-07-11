from django.db import models

# Create your models here.
class User(models.Model):
    
    class Role(models.TextChoices):
        REGULAR = 'Regular', 
        ADMIN = 'Admin'
    
    firstName = models.CharField(max_length = 100)
    lastName= models.CharField(max_length = 100)
    email = models.CharField(max_length =100,unique = True)
    number = models.CharField(max_length =13 ,null = False, blank =False, unique =True)
    role = models.CharField(max_length =8, choices = Role.choices, default = Role.REGULAR)
    
    def _str_(self):
        return self.email