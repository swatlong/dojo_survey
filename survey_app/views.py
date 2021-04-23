from django.shortcuts import render, redirect, HttpResponse


def index(request):
    return render(request, 'form.html')

def process(request):
    if request.method == 'GET':
        print('Method', request.method)
        return redirect('/')
    request.session ['name'] = request.POST['name']
    request.session ['loc'] = request.POST['location']
    request.session ['lang'] = request.POST['language']
    
    return redirect('/result')

def result(request):
    print(request.session)
    # context = {
    #   'name': request.session['name'],
    #   'loc': request.session['loc'],
    #   'lang': request.session['lang']
    # }
    return render(request,'result.html')
