from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  #return HttpResponse('home')
  return render(request, 'homepage.html') #takes two parameters request, what template we want to send back 


def about(request):
  #return HttpResponse('about')
  return render(request, 'about.html')