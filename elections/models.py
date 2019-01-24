from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.contenttypes.fields import GenericRelation

from candidates.models import Candidate
from shared.models import Section
from shared.states import make_states

class Election(models.Model):
    title = models.CharField(max_length=200)
    candidates = models.ManyToManyField(Candidate, related_name="elections")
    cover_image_url = models.URLField(null=True, blank=True)
    image_urls = ArrayField(models.URLField(), null=True, blank=True)
    sections = GenericRelation(Section)
    date = models.DateField()

    type_choices = (
        ('State', 'State'),
        ('National', 'National'),
        ('None', 'None')
    )
    type = models.CharField(
        max_length=10,
        choices=type_choices,
        default='None'
    )
    # This field is only relevant if the type is state
    state = models.CharField(
        max_length=20,
        choices = make_states(),
        default='None'
    )
    last_edited = models.DateField(auto_now=True)

    def __str__(self):
        if self.type == 'State':
            return self.title + " - " + self.type + " - " + self.state
        return self.title + " - " + self.type
