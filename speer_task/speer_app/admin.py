from django.contrib import admin

# Register your models here.
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display=('id', 'user', 'content', 'created_at')
admin.site.register(Note)