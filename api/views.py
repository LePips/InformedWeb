from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .serializers import CandidateSerializer, ElectionSerializer
from candidates.models import Candidate
from elections.models import Election

def candidates_list(request):
    candidates = Candidate.objects.all()
    serializer = CandidateSerializer(candidates, many=True)
    return JsonResponse(serializer.data, safe=False)

def candidate_detail(request, id):
    candidate = Candidate.objects.get(id=id)
    serializer = CandidateSerializer(candidate)
    return JsonResponse(serializer.data, safe=False)

def elections_list(request):
    elections = Election.objects.all()
    serializer = ElectionSerializer(elections, many=True)
    return JsonResponse(serializer.data, safe=False)

def election_detail(request, id):
    election = Election.objects.get(id=id)
    serializer = ElectionSerializer(election)
    return JsonResponse(serializer.data, safe=False)