from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "index.html"

def all_candidate(request):
    candidates = []
    return render( request,'retrieve_candidate.html', {"candidates": candidates})


def new_candidate(request):
    return render( request,'create_candidate.html', {})