from django.contrib import admin

from .models import Candidate
from shared.models import Section
from shared.admin import SectionInline

class ElectionsInline(admin.TabularInline):
    model = Candidate.elections.through
    extra = 1

class ContributorInline(admin.TabularInline):
    model = Candidate.contributors.through

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'last_edited', 'type', 'state')
    inlines = [ElectionsInline, SectionInline, ContributorInline]
    search_fields = ['first', 'last']
    exclude = ['elections']

    def full_name(self, obj):
        return obj.first + " " + obj.last

    # Lines are commented out for future reference
    # fields = ['first', 'elections', 'candidate_area_type']
    # list_filter = ['candidate_area_type']

admin.site.register(Candidate, CandidateAdmin)
