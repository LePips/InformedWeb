from django.contrib import admin

from .models import ElectionInfoRequest
from elections.models import Election
from shared.admin import SectionInline

class CandidatesInline(admin.TabularInline):
    model = ElectionInfoRequest.candidates.through
    extra = 1

class ElectionRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    inlines = [CandidatesInline, SectionInline]
    exclude = ['candidates']


admin.site.register(ElectionInfoRequest, ElectionRequestAdmin)
