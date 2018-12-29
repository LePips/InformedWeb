import string
import random
from django.shortcuts import render, redirect
from django.http import HttpResponse

from Firebase import Firebase
from .models import Candidate

def candidates_list(request):
    template = 'candidates_list.html'
    candidates = Firebase.instance().get_candidates()
    context = {'candidates': candidates}
    return render(request, template, context)

def view_candidate(request, id):
    # TODO
    return

def edit_candidate(request, id):
    template = 'edit_candidate.html'
    candidate = Firebase.instance().get_candidate(id)
    context = {'candidate': candidate}
    return render(request, template, context)

def set_candidate(request, id):
    first = request.POST['first_name']
    last = request.POST['last_name']
    image_url = request.POST['image_url']
    if len(image_url) < 5:
        image_url = None # Hack to get null

    sections = []
    for key in request.POST:
        if key.startswith("section_content_"):
            section = {}
            section["title"] = key[16:] # Hack
            section["content"] = request.POST[key]
            sections.append(section)
    candidate = Candidate(first=first,
                          last=last,
                          id=id,
                          image_url=image_url,
                          sections=sections)
    Firebase.instance().set_candidate(candidate)
    return redirect("/candidates")

def create_candidate(request):
    template = 'edit_candidate.html'
    id = id_generator()
    candidate = Candidate(first=None,
                          last=None,
                          id=id,
                          image_url=None,
                          sections=None)
    context = {'candidate': candidate}
    return render(request, template, context)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
