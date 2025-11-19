from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import MissionaryUpdatePage, MissionaryProfilePage, MissionaryNewsletterSignup

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

def missionary_newsletter_signup(request, slug):
    missionary = get_object_or_404(MissionaryProfilePage, slug=slug)
    if request.method == "POST":
        email = request.POST.get('email')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        if email:
            if not MissionaryNewsletterSignup.objects.filter(missionary=missionary, email=email).exists():
                MissionaryNewsletterSignup.objects.create(
                    missionary=missionary,
                    email=email,
                    first_name=first_name,
                    last_name=last_name
                )
                messages.success(request, "Thank you for signing up for updates!")
            else:
                messages.info(request, "You are already signed up for updates.")
        else:
            messages.error(request, "Please enter a valid email address.")
    return redirect(missionary.url)
