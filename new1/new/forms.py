from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
        
class admin_user(UserChangeForm):
    class Meta:
        model=User
        fields='__all__'
    
class user_form(UserChangeForm):
    class Meta:
        model=User
        fields=('username','first_name')
