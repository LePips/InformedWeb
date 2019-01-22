from django.contrib import admin

from .models import Election
from shared.models import Section
from shared.admin import SectionInline

class CandidatesInline(admin.TabularInline):
    model = Election.candidates.through
    extra = 1

class ContributorsInline(admin.TabularInline):
    model = Election.contributors.through

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

class ElectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'type')
    inlines = [CandidatesInline, SectionInline, ContributorsInline]
    search_fields = ['title']
    exclude = ['candidates']

admin.site.register(Election, ElectionAdmin)
