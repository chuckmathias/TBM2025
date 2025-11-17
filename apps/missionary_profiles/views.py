from django.shortcuts import render
from .models import MissionaryUpdatePage, MissionaryProfilePage

# Create your views here.

def master_updates_list(request):
    missionary_slug = request.GET.get('project')
    updates = MissionaryUpdatePage.objects.live().order_by('-first_published_at')
    missionaries = MissionaryProfilePage.objects.live().order_by('name')
    missionary = None
    if missionary_slug:
        missionary = missionaries.filter(slug=missionary_slug).first()
        if missionary:
            updates = updates.filter(missionary_profile=missionary)
    return render(request, 'missionary_profiles/master_updates_list.html', {
        'updates': updates,
        'missionary': missionary,
        'missionaries': missionaries,
    })
