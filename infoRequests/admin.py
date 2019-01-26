from django.contrib import admin

from .models import Contributor, ElectionInfoRequest, CandidateInfoRequest

class ElectionInfoRequestInline(admin.TabularInline):
    model = ElectionInfoRequest
    fk_name = "contributor"
    verbose_name = "Election Info Request"
    verbose_name_plural = "Election Info Requests"
    show_change_link = True
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

class CandidateInfoRequestInline(admin.TabularInline):
    model = CandidateInfoRequest
    fk_name = "contributor"
    verbose_name = "Candidate Info Request"
    verbose_name_plural = "Candidate Info Requests"
    show_change_link = True
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

class ContributorAdmin(admin.ModelAdmin):
    inlines = [ElectionInfoRequestInline, CandidateInfoRequestInline]
    exclude = ['elections', 'candidates']

class ElectionInfoRequestAdmin(admin.ModelAdmin):
    list_display = ('content', 'contributor', 'election')
    readonly_fields = ['contributor']
    search_fields = ['contributors', 'election']

class CandidateInfoRequestAdmin(admin.ModelAdmin):
    list_display = ('content', 'contributor', 'candidate')
    readonly_fields = ['contributor']
    search_fields = ['contributors', 'candidate']

admin.site.register(Contributor, ContributorAdmin)
admin.site.register(ElectionInfoRequest, ElectionInfoRequestAdmin)
admin.site.register(CandidateInfoRequest, CandidateInfoRequestAdmin)
