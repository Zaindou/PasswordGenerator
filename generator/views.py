from pydoc import render_doc
from django import views
from django.shortcuts import render
import random

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):


    characters = list('abcdefghijklmnopqrstvwxyz')
    generated_password = ''

    length = int(request.GET.get('length'))
    
    if request.GET.get('Uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!#$%&()*+,-./:;<=>?@[\]^_{}'))
    
    if request.GET.get('numbers'):
        characters.extend(list('123456789'))
    
    for char in range(length):
        generated_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': generated_password})




