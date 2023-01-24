from django.urls import path
from . import views
from .views import index, CollaboratorListView, CollaboratorDetailView

urlpatterns = [
    path("", CollaboratorListView.as_view(), name='collaborator_list'),
    path("developer/<int:pk>/", CollaboratorDetailView.as_view(), name = 'collaborator-detail'),
    path("register", views.register_request, name = "register"),
    path("logout", views.logout_request, name = "logout"),
    path("login", views.login_request, name = "login"),
]
