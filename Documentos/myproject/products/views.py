from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

@login_required
def product_list(request):
    # Fetches products that belong to the logged-in user
    products = Product.objects.filter(user=request.user)
    return render(request, 'products/product_list.html', {'products': products})

@login_required
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user  # Ensure the product is associated with the logged-in user
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_add.html', {'form': form})

@login_required
def product_delete(request, pk):
    Product.objects.get(id=pk).delete()
    return redirect('product_list')

