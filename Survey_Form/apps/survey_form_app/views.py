from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    try:
        request.session['counter']
    except:
        request.session['counter'] = 0
    return render(request, 'survey_form_app/index.html')

def process(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect('/result')
    else:
        return redirect('/')

def result(request):
    request.session['counter'] += 1
    return render(request, 'survey_form_app/result.html')
