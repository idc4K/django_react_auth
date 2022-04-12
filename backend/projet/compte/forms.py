from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import get_user_model




class formail(UserCreationForm):
    User = get_user_model()
    class Meta:
        model = get_user_model()
        fields = ('first_name','email', 'password1', 'password2')
        

