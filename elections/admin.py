from django.contrib import admin

from .models import Election
from shared.models import Section
from shared.admin import SectionInline

class CandidatesInline(admin.TabularInline):
    model = Election.candidates.through
    extra = 1

class ElectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    inlines = [CandidatesInline, SectionInline]
    exclude = ['candidates']

admin.site.register(Election, ElectionAdmin)
