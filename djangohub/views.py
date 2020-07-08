from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    dictionary = {
        
    }
    return render(request, 'homepage/index.html', context=dictionary)