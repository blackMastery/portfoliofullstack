from django.contrib import admin
from .models import Repo

# Register your models here.
@admin.register(Repo)
class RepoAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')