from django.contrib import admin
from .models import ChurchMission

@admin.register(ChurchMission)
class ChurchMissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date')