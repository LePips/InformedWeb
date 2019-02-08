from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from shared.models import Section

class Article(models.Model):
    title = models.CharField(max_length=100)
    sections = GenericRelation(Section)
    last_edited = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
