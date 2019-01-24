from django.db import models

class TextAnnouncement(models.Model):
    announcement = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    show_on_launch = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.announcement[:30] + "..."
