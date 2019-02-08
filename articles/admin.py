from django.contrib import admin

from .models import Article
from shared.admin import SectionInline

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    inlines = [SectionInline]

admin.site.register(Article, ArticleAdmin)
