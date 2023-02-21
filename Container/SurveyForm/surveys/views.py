from django.shortcuts import render, redirect

def survey(request):
    return render(request, 'survey.html')

def process(request):
    if request.method == "POST":
        # Process the form data
        request.session['counter'] = request.session.get('counter', 0) + 1
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']

        return redirect('/result')
    else:
        # If the user tries to access this page via GET, redirect them to the homepage
        return redirect('/')

def result(request):
    return render(request, 'result.html')
