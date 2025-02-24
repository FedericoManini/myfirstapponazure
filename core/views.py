from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.contrib import messages
from .forms import ProductForm
# Create your views here.


def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "pages/home.html", context)


def createProducts(request):
    form = ProductForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            messages.success(request, "Prodotto creato con successo")
            form = ProductForm()
        else:
            messages.warning(request, "Controlla i campi richiesti")

    return render(request, "pages/create_product.html", {'form': form})
