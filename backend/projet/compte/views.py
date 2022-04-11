from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render("<h1>Hello world</h1>")
# Create your views here.
