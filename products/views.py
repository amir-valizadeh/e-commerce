from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):
    products=Product.objects.all()
    return render(request, 'products/landingPage.html',{'products':products})

def product(request,pk):
    product = Product.objects.get(pk=pk)
    print("here",product.id)
    return render(request, 'products/product.html',{'product':product})