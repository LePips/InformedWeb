from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    template = 'home.html'
    return render(request, template)
