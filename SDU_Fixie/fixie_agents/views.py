from django.shortcuts import render


def home(request):
    return render(request, "fixie_agents/home.html")


def scopus_metrics(request):
    return render(request, "fixie_agents/scopus_metrics.html")


def react(request):
    return render(request, "fixie_agents/react.html")


def django(request):
    return render(request, "fixie_agents/django.html")
