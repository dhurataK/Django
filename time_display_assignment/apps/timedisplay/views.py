from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    day_format = "%b %d, %Y"
    time_format = "%I:%M %p"
    today = datetime.datetime.today()
    day = today.strftime(day_format)
    time = today.strftime(time_format)
    return render(request, "timedisplay/index.html",{'day':day, 'time':time})
