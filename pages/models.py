from django.db import models
from django.utils import timezone



class Project(models.Model):
    title = models.CharField(max_length=200)
    budget = models.DecimalField(max_digits=10, decimal_places=1)
    description = models.TextField(max_length=3000)
    start_date = models.DateField(auto_now=False)
    finish_date = models.DateField(auto_now=False)

    class Meta:
        ordering = ['budget']

