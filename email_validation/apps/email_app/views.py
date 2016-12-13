from django.shortcuts import render,redirect
from .models import Email
# Create your views here.
def index(request):
    return render(request, 'email_app/index.html')

def store(request):
    if request.method == 'POST':
        check = Email.emailManager.validate(request.POST['email'])
        if check[0] == False:
            request.session['wrong'] = check[1]
            return redirect('/')
        elif check[0] == True:
            Email.objects.create(email =request.POST['email'])
            request.session['right'] = check[1]
            return redirect('/success')
        else:
            request.session.clear()
            return redirect('/')
    elif request.method == 'GET':
        request.session.clear()
        return redirect('/')

def success(request):
    context ={
        'emails': Email.objects.all()
    }
    return render(request, 'email_app/success.html', context)

def delete(request, id):
    email = Email.objects.get(id=id)
    request.session['right'] = 'Email:{} deleted successfuly'.format(email.email)
    email.delete()
    return redirect('/success')
