"""
URL configuration for SDU_Fixie project.

"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("fixie_agents.urls")),  # Include the app's URLs at the root
]
