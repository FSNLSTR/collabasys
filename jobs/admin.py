from django.contrib import admin
from .models import Collaborator, Enterprise

# Register your models here.
admin.site.register(Collaborator)
admin.site.register(Enterprise)