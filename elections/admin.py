from django.contrib import admin

from .models import Election
from shared.models import Section
from shared.admin import SectionInline
from infoRequests.models import ElectionInfoRequest

class CandidatesInline(admin.TabularInline):
    model = Election.candidates.through
    extra = 1
    verbose_name = "Candidate"
    verbose_name_plural = "Candidates"

class ContributorsInline(admin.TabularInline):
    model = Election.contributors.through
    verbose_name = "Contributor"
    verbose_name_plural = "Contributors"

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

class InfoRequestsInline(admin.TabularInline):
    model = ElectionInfoRequest
    fk_name = "election"
    verbose_name = "Info Request"
    verbose_name_plural = "Info Requests"
    show_change_link = True

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

class ElectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'type', 'state')
    inlines = [CandidatesInline, SectionInline,
               ContributorsInline, InfoRequestsInline]
    search_fields = ['title']
    exclude = ['candidates']

admin.site.register(Election, ElectionAdmin)
