from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(r):
    return HttpResponse("<h1> Welcome to Home Page </h>")
