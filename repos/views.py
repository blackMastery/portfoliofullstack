from django.shortcuts import render
from .models import Repo
from django.views.generic import ListView

# Create your views here.

class RepoListView(ListView):
    queryset = Repo.objects.all()
    context_object_name = 'repos'
    paginate_by = 3
    template_name = 'repos/list.html'