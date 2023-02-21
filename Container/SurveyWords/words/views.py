from django.shortcuts import render, redirect

def add_word(request):
    if request.method == 'POST':
        word = request.POST['word']
        color = request.POST.get('color', 'black')
        font_size = request.POST.get('font_size', 'normal')
        request.session[word] = {'color': color, 'font_size': font_size}
        return redirect('/')
    else:
        return render(request, 'add_word.html')

def clear(request):
    if request.method == 'POST':
        request.session.clear()
        return redirect('/')
    else:
        return render(request, 'clear.html')

def index(request):
    words = request.session.items()
    return render(request, 'index.html', {'words': words})
