from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'disappearing_ninjas_app/index.html')

def show_ninjas(request, ninja_color):
    result ={}
    if ninja_color == "":
        result = {'ninja': 'all'}
    else:
        ninjas = {
                'orange':'michelangelo',
                'red':'raphael',
                'blue':'leonardo',
                'purple':'donatello'
        }
        if ninja_color in ninjas:
            result['ninja'] = ninjas[ninja_color]
        else:
            result['ninja'] = 'notapril'
    return render(request, 'disappearing_ninjas_app/ninjas.html', result)
