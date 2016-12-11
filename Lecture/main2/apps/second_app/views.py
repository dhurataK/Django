from django.shortcuts import render
from .models import People
# Create your views here.
def index(request):
    People.objects.create(first_name ="Mike", last_name = "Hannon")
    people = People.objects.all()
    print people
    return render(request, 'second_app/index.html')
