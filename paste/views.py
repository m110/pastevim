from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'paste/index.html', context)

def add(request):
    pass

def view(request, url_hash, theme_name):
    context = {
        'url_hash' : url_hash,
        'theme_name' : theme_name,
    }
    return render(request, 'paste/view.html', context)

def delete(request):
    pass
