from django.db import models
from django.contrib.postgres import fields
from django.contrib.contenttypes.fields import GenericRelation

from candidates.models import Candidate
from shared.models import Section

class Election(models.Model):
    title = models.CharField(max_length=200)
    candidates = models.ManyToManyField(Candidate, related_name="elections")
    cover_image_url = models.URLField(null=True, blank=True)
    image_urls = fields.ArrayField(models.URLField(), null=True, blank=True)
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
    last_edited = models.DateField(auto_now=True)

    def __str__(self):
        return self.title + " - " + self.election_area_type
