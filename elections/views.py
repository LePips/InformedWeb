import string
import random
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Election

def elections_list(request):
    # template = 'elections_list.html'
    # elections = Firebase.instance().get_elections()
    # context = {'elections': elections}
    # return render(request, template, context)
    return HttpResponse("This isn't finished yet")

def view_election(request):
    # TODO
    return

def edit_election(request, id):
    # template = 'edit_election.html'
    # election = Firebase.instance().get_election(id)
    # context = {'election': election}
    # return render(request, template, context)
    return HttpResponse("This isn't finished yet")

def set_election(request, id):
    # title = request.POST['title']
    # category = request.POST['category']
    # cover_image_url = request.POST['cover_image_url']
    # if len(cover_image_url) < 5:
    #     cover_image_url = None # Hack to get null
    #
    # sections = []
    # for key in request.POST:
    #     if key.startswith("section_content_"):
    #         section = {}
    #         section["title"] = key[16:] # Hack
    #         section["content"] = request.POST[key]
    #         sections.append(section)
    #
    # election = Election(id=id,
    #                     title=title,
    #                     category=category,
    #                     cover_image_url=cover_image_url,
    #                     sections=sections)
    # Firebase.instance().set_election(election)
    # return redirect("/elections")
    return HttpResponse("This isn't finished yet")

def create_election(request):
    # template = 'edit_election.html'
    # id = id_generator()
    # election = Election(id=id,
    #                     title=None,
    #                     category=None,
    #                     cover_image_url=None,
    #                     sections=None)
    # context = {'election': election}
    # return render(request, template, context)
    return HttpResponse("This isn't finished yet")

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
