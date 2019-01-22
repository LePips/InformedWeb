from django.db import models
from django.contrib.postgres import fields
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

from elections.models import Election
from candidates.models import Candidate
from shared.models import Section

class Contributor(models.Model):
    username = models.CharField(max_length=15)
    elections = models.ManyToManyField(Election, related_name="contributors", blank=True)
    candidates = models.ManyToManyField(Candidate, related_name="contributors", blank=True)

    def __str__(self):
        return self.username
