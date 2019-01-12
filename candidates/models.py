from django.db import models
from django.contrib.postgres import fields
from django.contrib.contenttypes.fields import GenericRelation

from shared.models import Section

class Candidate(models.Model):
    first = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    cover_image_url = models.URLField(null=True, blank=True)
    image_urls = fields.ArrayField(models.URLField(), null=True, blank=True)
    sections = GenericRelation(Section)

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
    last_edited = models.DateField(auto_now=True)

    def __str__(self):
        return self.first + " " + self.last
