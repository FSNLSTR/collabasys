from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from jobs.models import Collaborator

# Create your views here.
def index(request):
    return HttpResponse("<h1>Collabasys</h1>")

class CollaboratorListView(ListView):
    model = Collaborator

class CollaboratorDetailView(DetailView):
    model = Collaborator



