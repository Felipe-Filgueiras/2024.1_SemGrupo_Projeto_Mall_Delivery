from django import forms
from .models import UserProfile
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image']
        labels = {
            'name': 'Nome',  # Change these as per your language or preference
            'description': 'Descrição',
            'price': 'Preço',
            'category': 'Categoria',
            'image': 'Imagem'
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'cnpj', 'profile_picture', 'bank_account']