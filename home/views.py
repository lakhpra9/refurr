from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    context = {}
    return render(request, 'home/index.html', context=context)