from django.contrib import admin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import force_text
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Section
from .roles import Role, CandidateRole

class SectionInline(GenericTabularInline):
    model = Section
    extra = 0

class CandidateRoleInline(admin.TabularInline):
    model = CandidateRole
    extra = 0
    fields = ['role', 'start_date', 'end_date']
    readonly_fields = ['role', 'start_date', 'end_date']
    show_change_link = True

class CandidateRoleAdmin(admin.ModelAdmin):
    inlines = [SectionInline]
    exclude = ['candidate']

class RoleAdmin(admin.ModelAdmin):
    inlines = [SectionInline]

admin.site.register(Role, RoleAdmin)
admin.site.register(CandidateRole, CandidateRoleAdmin)
