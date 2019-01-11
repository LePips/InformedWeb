from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Section

class SectionInline(GenericTabularInline):
    model = Section
    extra = 0
