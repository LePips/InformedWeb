from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from elections.models import Election
from candidates.models import Candidate
from shared.models import Section
from shared.states import make_states

class Contributor(models.Model):
    username = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    elections = models.ManyToManyField(Election, related_name="contributors",
                                       blank=True)
    candidates = models.ManyToManyField(Candidate, related_name="contributors",
                                        blank=True)

    def __str__(self):
        return self.username

class ElectionInfoRequest(models.Model):
    content = models.TextField(max_length=800)
    contributor = models.ForeignKey(Contributor, on_delete=models.SET_NULL,
                                    related_name="electionInfoRequests",
                                    blank=True, null=True)
    election = models.ForeignKey(Election, on_delete=models.SET_NULL,
                                 related_name="infoRequests",
                                 blank=True, null=True)

    def __str__(self):
        return self.content[:30]

class CandidateInfoRequest(models.Model):
    content = models.TextField(max_length=800)
    contributor = models.ForeignKey(Contributor, on_delete=models.SET_NULL,
                                    related_name="candidateInfoRequests",
                                    blank=True, null=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.SET_NULL,
                                 related_name="infoRequests",
                                 blank=True, null=True)

    def __str__(self):
        return self.content[:30]
