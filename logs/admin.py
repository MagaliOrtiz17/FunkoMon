from django.contrib import admin
from .models import Log

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'is_correct', 'created')
    list_filter = ('is_correct', 'created')