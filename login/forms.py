from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# specify more field for user registration form
class UserRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


        
