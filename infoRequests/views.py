from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from candidates.models import Candidate
from elections.models import Election
from .models import Contributor, ElectionInfoRequest, CandidateInfoRequest

# This is a horrible implementation.
@csrf_exempt
def create_info_request(request):
    data = request.POST

    if not data:
        return HttpResponse(status=400)

    import ipdb; ipdb.set_trace()

    try:
        model = None
        content = data['content']
        contributor_id = data['contributor']
        contributor = Contributor.objects.get(id=contributor_id)
        model_id = None
        if data['type'] == 'election':
            model_id = data['model_id']
            election = Election.objects.get(id=model_id)
            model = ElectionInfoRequest(content=content, contributor=contributor, election=election)
        else:
            model_id = data['model_id']
            candidate = Candidate.objects.get(id=model_id)
            model = CandidateInfoRequest(content=content, contributor=contributor, candidate=candidate)

        if model:
            model.save()
            return HttpResponse(status=201)
        return HttpResponse(status=400)
    except:
        return HttpResponse(status=400)
