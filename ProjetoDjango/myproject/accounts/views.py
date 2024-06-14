from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def landing_page(request):
    products = Product.objects.all()
    return render(request, 'accounts/landing_page.html', {'products': products})

from django.shortcuts import render
from products.models import Product

def user_product_list(request):
    products = Product.objects.filter(user=request.user)
    return render(request, 'accounts/product_list.html', {'products': products})