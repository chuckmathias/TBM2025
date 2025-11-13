from django.shortcuts import render
from .models import MissionaryUpdatePage

# Create your views here.

def master_updates_list(request):
    updates = MissionaryUpdatePage.objects.live().order_by('-first_published_at')
    return render(request, 'missionary_profiles/master_updates_list.html', {
        'updates': updates,
    })
