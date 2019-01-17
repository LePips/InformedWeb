from django.shortcuts import render, redirect
from django.http import HttpResponse

# 1-16-19
# Use the Admin page for all adding and editing of data
def home(request):
    return redirect("/admin")
