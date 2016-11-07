from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
# Create your views here.
def index(request):
    try:
        request.session['attempts']
    except:
        request.session['attempts'] = 0
    return render(request,'random_word_app/index.html')

def generate(request):
    if request.method == "POST":
        request.session['attempts'] += 1
        request.session['word'] = get_random_string(length=14)
        return redirect('/')

def reset(request):
    if request.method == "POST":
        request.session['attempts'] = 0
        return redirect('/')
