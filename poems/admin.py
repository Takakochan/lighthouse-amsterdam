from django.contrib import admin
from .models import Poem

@admin.register(Poem)
class PoemAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_published', 'created_at']
    list_filter = ['is_published']
    search_fields = ['title', 'author__username']
