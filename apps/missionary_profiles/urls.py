from django.urls import path
from . import views

urlpatterns = [
    # ... other patterns ...
    path('all-updates/', views.master_updates_list, name='master_updates_list'),
]