from django.shortcuts import render, HttpResponse, redirect
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib import messages
from django.views.generic import ListView, DetailView
from jobs.models import Collaborator
# Create your views here.
def index(request):
    return HttpResponse("<h1>Collabasys</h1>")

def logout_request(request):
    logout(request)
    messages.info(request, "Logged Out Successfully")
    return redirect("collaborator_list")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user, backend = 'django.contrib.auth.backends.ModelBackend')
                messages.info(request, f"You are now logged in as {username}")
                return redirect('collaborator_list')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request = request, template_name= "jobs/login.html", context={"form":form})

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend = 'django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Registration Successful.")
            return redirect("collaborator_list")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request = request, template_name = "jobs/register.html", context={"register_form":form})

class CollaboratorListView(ListView):
    model = Collaborator

class CollaboratorDetailView(DetailView):
    model = Collaborator



