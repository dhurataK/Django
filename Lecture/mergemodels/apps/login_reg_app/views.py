from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User
# Create your views here.
def index(request):
    user = User.objects.all()
    context = {
        'user':user
    }
    return render(request, 'login_reg_app/index.html', context)

def success(request):
    return render(request,'login_reg_app/success.html')

def register(request):
    if request.method == 'POST':
        result = User.objects.register_validations(request.POST)
        if not result[0]:
            for error in result[1]:
                messages.error(request, error)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        result = User.objects.login_validations(request.POST)
        if result[0]:# if result[0] == True
            request.session['first_name'] = result[1].first_name
            return redirect('/success')
        else:
            for error in result[1]:
                messages.error(request, error)
            return redirect('/')
