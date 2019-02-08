from django.contrib import admin

from .models import Candidate
from shared.models import Section
from shared.admin import SectionInline, CandidateRoleInline
from infoRequests.models import CandidateInfoRequest

class ElectionsInline(admin.TabularInline):
    model = Candidate.elections.through
    extra = 1
    verbose_name = "Election"
    verbose_name_plural = "Elections"

class ContributorInline(admin.TabularInline):
    model = Candidate.contributors.through
    verbose_name = "Contributor"
    verbose_name_plural = "Contributors"

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

class InfoRequestsInline(admin.TabularInline):
    model = CandidateInfoRequest
    fk_name = "candidate"
    verbose_name = "Info Request"
    verbose_name_plural = "Info Requests"
    show_change_link = True

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'last_edited', 'type', 'state')
    inlines = [ElectionsInline, SectionInline,
               CandidateRoleInline, InfoRequestsInline]
    search_fields = ['first', 'last']
    exclude = ['elections']

    def full_name(self, obj):
        return obj.first + " " + obj.last

    # Lines are commented out for future reference
    # fields = ['first', 'elections', 'candidate_area_type']
    # list_filter = ['candidate_area_type']

admin.site.register(Candidate, CandidateAdmin)
