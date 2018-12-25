from django.db import models

# Create your models here.
class Candidate():
    def __init__(self, first, last, id):
        self.id = id
        self.first = first
        self.last = last

    def to_dict(self):
        return {u'first': self.first, u'last': self.last, u'id': self.id}
