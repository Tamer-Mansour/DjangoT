from django.shortcuts import render

import random
from django.shortcuts import render

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, 'index.html')

def process_gold(request):
    building = request.POST['building']
    if building == 'farm':
        gold = random.randint(10, 20)
        request.session['gold'] += gold
        message = f'Earned {gold} golds from the farm!'
    elif building == 'cave':
        gold = random.randint(5, 10)
        request.session['gold'] += gold
        message = f'Earned {gold} golds from the cave!'
    elif building == 'house':
        gold = random.randint(2, 5)
        request.session['gold'] += gold
        message = f'Earned {gold} golds from the house!'
    elif building == 'casino':
        gold = random.randint(-50, 50)
        request.session['gold'] += gold
        if gold < 0:
            message = f'Entered a casino and lost {abs(gold)} golds... Ouch..'
        else:
            message = f'Entered a casino and won {gold} golds!'
    request.session['activities'].append(message)
    return render(request, 'index.html')
