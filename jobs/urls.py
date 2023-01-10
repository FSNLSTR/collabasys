from django.urls import path
from .views import index, CollaboratorListView, CollaboratorDetailView

urlpatterns = [
    path("", CollaboratorListView.as_view(), name='collaborator_list'),
    path("developer/<int:pk>/", CollaboratorDetailView.as_view(), name = 'collaborator-detail'),
]