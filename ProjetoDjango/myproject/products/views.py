from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

@login_required
def product_list(request):
    products = Product.objects.filter(user=request.user)
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user 
            product.save()
            return redirect('product_list')
    return render(request, 'products/product_list.html', {'products': products, 'form': form})

@login_required
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user 
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_add.html', {'form': form})

@login_required
def product_delete(request, pk):
    Product.objects.get(id=pk).delete()
    return redirect('product_list')

