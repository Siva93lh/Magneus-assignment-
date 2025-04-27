from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'home.html')

def tabs(request):
    return render(request, 'tabs.html')

def autocomplete(request):
    return render(request, 'autocomplete.html')

def collapsible(request):
    return render(request, 'collapsible.html')

def images(request):
    return render(request, 'images.html')

def slider(request):
    return render(request, 'slider.html')

def tooltips(request):
    return render(request, 'tooltips.html')

def popups(request):
    return render(request, 'popups.html')

def links(request):
    return render(request, 'links.html')

def css_properties(request):
    return render(request, 'css_properties.html')

def frames(request):
    return render(request, 'frames.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
