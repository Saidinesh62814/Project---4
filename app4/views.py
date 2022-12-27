from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def second(request):
    return HttpResponse("<h1> This is the worst and beautiful </h1") 