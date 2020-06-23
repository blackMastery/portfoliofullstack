from django.urls import path
from . import views

app_name = 'repos'

urlpatterns = [
    path('', views.RepoListView.as_view(), name='repo_list'),

]