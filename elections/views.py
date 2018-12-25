from django.shortcuts import render, redirect
from django.http import HttpResponse

from Firebase import Firebase


def elections_list(request):
    template = 'elections_list.html'
    ids = Firebase.instance().get_election_ids()
    context = {'ids': ids}
    return render(request, template, context)

def edit_election(request, id):
    template = 'edit_election.html'
    election = Firebase.instance().get_election(id)
    context = {'election': election}
    return render(request, template, context)
