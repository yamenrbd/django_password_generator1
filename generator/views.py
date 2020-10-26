from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request , 'generator/home.html')


def password(request):

    thepassword = ''

    character = list('abcdefghijklmnopqrstuvwxyz')
    #length = 12
    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('number'):
        character.extend(list('0123456789'))

    if request.GET.get('special'):
        character.extend(list('!@#$%^&*()'))
    

    for i in range(length):
        
        thepassword += random.choice(character)



    return render(request , 'generator/password.html', {'password':thepassword})

def about(request):
    
    return render(request , 'generator/about.html')