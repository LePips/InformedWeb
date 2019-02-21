from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.contenttypes.fields import GenericRelation

from shared.models import Section
from shared.states import make_states

class Candidate(models.Model):
    first = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    cover_image_url = models.URLField(null=True, blank=True)
    image_urls = ArrayField(models.URLField(), null=True, blank=True)
    sections = GenericRelation(Section)
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    wikipedia = models.URLField(null=True, blank=True)
    last_edited = models.DateField(auto_now=True)

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
    party_choices = (
        ('Democrat', 'Democrat'),
        ('Republican', 'Republican'),
        ('Independent', 'Independent'),
        ('Other', 'Other'),
        ('None', 'None')
    )
    party = models.CharField(
        max_length=15,
        choices=party_choices,
        default='None'
    )
    # This field is only relevant if the party type is 'Other'
    other_party = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.first + " " + self.last
