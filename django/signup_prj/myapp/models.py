from django.db import models
import uuid
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_superuser(self, password, **kwargs):
        user = self.model(is_superuser=True, **kwargs)    
        user.password = make_password(password)    
        user.save()    
        return user
   

class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=150, null=True, blank=True)
    phone = models.PositiveIntegerField(unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    password = models.CharField(max_length=150, unique=True, null=True, blank=True)
    otp=models.CharField(max_length=10,null=True,blank=True)
    verify=models.BooleanField(null=True,blank=True)
    is_eligible = models.BooleanField(null=True, blank=True)
    is_valid = models.BooleanField(default=True, null=True, blank=True)
    is_staff = models.BooleanField(default=True, null=True, blank=True)

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'

    groups = None  
    user_permissions = None  

    def __str__(self):
        return self.email

    class Meta: 
        db_table = 'myapp'
