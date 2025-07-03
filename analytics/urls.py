from django.urls import path
from .views import track_profile_view

urlpatterns = [
    path('track-profile/', track_profile_view),
]
