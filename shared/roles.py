from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from shared.models import Section
from shared.states import make_states
from candidates.models import Candidate

class Role(models.Model):
    title = models.CharField(max_length=50)
    sections = GenericRelation(Section)
    serving_length = models.CharField(max_length=50)

    type_choices = (
        ('State', 'State'),
        ('National', 'National'),
        ('Other', 'Other'),
        ('None', 'None')
    )
    type = models.CharField(
        max_length=10,
        choices=type_choices,
        default='None'
    )
    # This field is only relevant if the candidate type is 'State'
    state = models.CharField(
        max_length=20,
        choices = make_states(),
        default='None'
    )

    def __str__(self):
        return self.title

class CandidateRole(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    sections = GenericRelation(Section)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self):
        return self.candidate.first + " " + self.candidate.last + " - " + self.role.title
