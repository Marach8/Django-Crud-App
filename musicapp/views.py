from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, I am so happy to create my own Django project today')