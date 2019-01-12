from django.contrib import admin

from .models import Candidate
from shared.models import Section
from shared.admin import SectionInline

class ElectionsInline(admin.TabularInline):
    model = Candidate.elections.through
    extra = 1

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'last_edited', 'type')
    inlines = [ElectionsInline, SectionInline]
    exclude = ['elections']

    def full_name(self, obj):
        return obj.first + " " + obj.last

    # Lines are commented out for future reference
    # children = serializers.StringRelatedField(many=True, read_only=True)
    # fields = ['first', 'elections', 'candidate_area_type']
    # list_filter = ['candidate_area_type']
    # search_fields = ['first']

admin.site.register(Candidate, CandidateAdmin)
