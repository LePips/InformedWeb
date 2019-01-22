from django.db import models

from elections.models import Election
from candidates.models import Candidate

class Contributor(models.Model):
    username = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    elections = models.ManyToManyField(Election, related_name="contributors",
                                       blank=True)
    candidates = models.ManyToManyField(Candidate, related_name="contributors",
                                        blank=True)

    def __str__(self):
        return self.username
