# fixie_agents/urls.py


from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # For http://127.0.0.1:8000/
    path("home/", views.home, name="home"),  # For http://127.0.0.1:8000/home/
    path("scopus_metrics/", views.scopus_metrics, name="scopus_metrics"),
    path("react/", views.react, name="react"),
    path("django/", views.django, name="django"),
]
