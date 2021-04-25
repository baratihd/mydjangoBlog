from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    #return HttpResponse('Hi there!')
    return render(request, 'about.html')

def home(request):
    #return HttpResponse('Hi there! thank you for back to home')
    return render(request, 'home.html')
