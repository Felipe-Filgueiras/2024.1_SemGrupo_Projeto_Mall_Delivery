from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'cnpj', 'cpf', 'date_of_birth', 'social_media_url', 'store_address', 'banner_image', 'profile_picture', 'bank_account', 'bank_agency', 'password1', 'password2')
