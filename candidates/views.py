from django.shortcuts import render, redirect
from django.http import HttpResponse

from Firebase import Firebase
from .models import Candidate

def candidates_list(request):
    template = 'candidates_list.html'
    ids = Firebase.instance().get_candidate_ids()
    context = {'ids': ids}
    return render(request, template, context)

def edit_candidate(request, id):
    template = 'edit_candidate.html'
    candidate = Firebase.instance().get_candidate(id)
    context = {'candidate': candidate}
    return render(request, template, context)

def set_candidate(request, id):
    first = request.POST['first']
    last = request.POST['last']
    candidate = Candidate(first, last, id)
    Firebase.instance().set_candidate(candidate)
    return HttpResponse("Set candidate with data: {}".format(candidate))
