from .models import CustomUser
from django.db.models import Q

def user_validation(email,password):
    obj=CustomUser.objects.filter(Q(email=email) & Q(password=password))
    if len(obj)==0:
        return False
    else:
        return True