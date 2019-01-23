from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .serializers import CandidateSerializer, ElectionSerializer
from candidates.models import Candidate
from elections.models import Election

def candidates_list(request):
    """
    Returns candidates under 'ids' or all elections if there are none
    specified
    """
    candidates = []

    if request.GET.get('ids'):
        ids = request.GET.get('ids')
        ids = ids.split(',')
        ids = filter(None, ids)
        for id in ids:
            candidate = Candidate.objects.get(id=id)
            candidates.append(candidate)
    else:
        candidates = Candidate.objects.all()

    serializer = CandidateSerializer(candidates, many=True)
    return JsonResponse({"candidates": serializer.data}, safe=False)

def candidate_detail(request, id):
    """
    Returns candidate with id
    """
    candidate = Candidate.objects.get(id=id)
    serializer = CandidateSerializer(candidate)
    return JsonResponse(serializer.data, safe=False)

def election_candidates(request, id):
    """
    Returns the candidates belonging to an election with id
    """
    election = Election.objects.get(id=id)
    candidates = election.candidates.all()
    serializer = CandidateSerializer(candidates, many=True)
    json = { "election_id": id,  "candidates": serializer.data}
    return JsonResponse(json, safe=False)

def elections_list(request):
    """
    Returns elections under 'ids' or all elections if there are none
    specified
    """
    elections = []
    ids = request.GET.get('ids')

    if ids:
        ids = ids.split(',')
        ids = filter(None, ids)
        for id in ids:
            election = Election.objects.get(id=id)
            elections.append(election)
    else:
        elections = Election.objects.all()

    serializer = ElectionSerializer(elections, many=True)
    return JsonResponse({"elections": serializer.data}, safe=False)

def election_detail(request, id):
    """
    Returns election with id
    """
    election = Election.objects.get(id=id)
    serializer = ElectionSerializer(election)
    return JsonResponse(serializer.data, safe=False)

def candidate_elections(request, id):
    """
    Returns the elections belonging to an candidate with id
    """
    candidate = Candidate.objects.get(id=id)
    elections = candidate.elections.all()
    serializer = ElectionSerializer(elections, many=True)
    json = { "candidate_id": id,  "elections": serializer.data}
    return JsonResponse(json, safe=False)
