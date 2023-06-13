from django.urls import path
from profiles.views import create_profile, update_profile,get_profile

urlpatterns = [
    path('api/profiles/', create_profile),
    path('api/profiles/<int:pk>/', update_profile),
    path('api/get_profiles/<int:pk>/', get_profile),
]
