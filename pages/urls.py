from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(),name='home' ),
    path('contact/', views.Contact.as_view(),name='contact' ),
    path('projects/', views.Projects.as_view(),name='projects' ),
    path('services/', views.Services.as_view(),name='services' ),


]