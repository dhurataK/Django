from django.shortcuts import render, redirect
import random, datetime
# Create your views here.
def index(request):
    try:
        request.session['gold']
    except:
        request.session['gold'] = 0
    try:
        request.session['activities']
    except:
        request.session['activities'] = []
    return render(request,'ninja_gold_app/index.html')

def ninja_gold(request):
    if request.method == "POST":
        now = datetime.datetime.now()
        time = now.strftime("%Y-%m-%d %H:%M")
        buildings = {
         'farm':random.randint(10,20),
         'cave':random.randint(5,10),
         'house':random.randint(2,5),
         'casino':random.randint(-50,50)
        }
        building = request.POST['building']
        if building in buildings:
            gold_gained_or_lost = buildings[building]
            request.session['gold'] += gold_gained_or_lost
            activity_result = {
                'color':('red','green') [gold_gained_or_lost > 0 ],
                'activity':('Entered a '+building+' and lost '+str(-(gold_gained_or_lost))+' golds...OUCH! ('+time+')','Earned '+str(gold_gained_or_lost)+' golds from the '+building+'! ('+time+')')[gold_gained_or_lost>0]
            }
            request.session['activities'].append(activity_result)
            return redirect('/')
