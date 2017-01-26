from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from .models import User
from ..books_app.models import Review, Book
# Create your views here.
def index(request):
    return render(request, 'login_reg_app/index.html')

def success(request):
    if not 'user' in request.session:
        return redirect(reverse('login_reg:index'))
    else:
        reviews = Review.objects.all().order_by('-id')[:3]
        books = Book.objects.all()
        context = {
            'reviews': reviews,
            'books':books
        }
        return render(request, 'books_app/index.html', context)

def register(request):
    if request.method == 'POST':
        user = User.objects.register_validation(request.POST)
        if not user[0]:
            for error in user[1]:
                messages.error(request, error)
    return redirect(reverse('login_reg:index'))

def login(request):
    if request.method == 'POST':
        user = User.objects.login_validation(request.POST)
        if user[0]:# if result[0] == True
            return log_user_in(request, user[1])
        else:
            for error in user[1]:
                messages.error(request, error)
            return redirect(reverse('login_reg:index'))

def log_user_in(request, user):
    request.session['user'] = {
        'id' : user.id,
        'first_name' : user.first_name,
        'alias' : user.alias,
        'email' : user.email,
    }
    return redirect(reverse('login_reg:success'))

def logout(request):
    request.session.pop('user')
    return redirect(reverse('login_reg:index'))
