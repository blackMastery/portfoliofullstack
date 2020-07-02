from django.contrib import admin
from .models import Intros


# Register your models here.
@admin.register(Intros)
class IntrosAdmin(admin.ModelAdmin):
    list_display = ('statement', 'status','publish')