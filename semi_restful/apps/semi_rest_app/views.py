from django.shortcuts import render, redirect
from models import Product
# Functions here will delegate to the correct method based on the HTMl verb

def products(request):
    if request.method == "POST":
        return create(request)
    #Else it's a GET, send to index method to return HTML
    return index(request)

def products_with_id(request,id):
    if request.method == "POST":
        return update(request, id)
    return show(request, id)

#******************************************************************
#GET /products
def index(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'semi_rest_app/index.html', context)

#POST products
def create(request):
    Product.objects.create(name = request.POST['name'], description = request.POST['description'], price = request.POST['price'])
    return redirect('/products')

# GET /products/new
def new(request):
    return render(request, 'semi_rest_app/new.html')

# GET / products/show/<id>
def show(request, id):
    product = Product.objects.get(id = id)
    context = {
        'product': product
    }
    return render(request, 'semi_rest_app/show.html', context)

#POST /products/<id>
def update(request, id):
    # update logic to ProductManager
    Product.objects.update(id, request.POST)
    return redirect('/products')

# GET /products/<id>/edit
def edit(request, id):
    product = Product.objects.get(id = id)
    context = {
        'product' :product
    }
    return render(request, 'semi_rest_app/edit.html', context)

# POST /products/<id>/destroy
def destroy(request,id):
    Product.objects.get(id = id).delete()
    return redirect('/products')
