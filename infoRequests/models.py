from django.db import models
from django.contrib.postgres import fields
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

from elections.models import Election
from candidates.models import Candidate
from shared.models import Section

class ElectionInfoRequest(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    candidates = models.ManyToManyField(Candidate, related_name="info_request_elections", blank=True)
    cover_image_url = models.URLField(null=True, blank=True)
    image_urls = fields.ArrayField(models.URLField(), null=True, blank=True)
    sections = GenericRelation(Section)
    date = models.DateField(null=True, blank=True)

    type_choices = (
        ('State', 'State'),
        ('National', 'National'),
        ('None', 'None')
    )
    type = models.CharField(
        max_length=10,
        choices=type_choices,
        default='None',
        null=True,
        blank=True
    )
    last_edited = models.DateField(auto_now=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
