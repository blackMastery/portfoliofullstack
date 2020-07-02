from django.db import models
from django.utils import timezone



class Project(models.Model):
    title = models.CharField(max_length=200)
    budget = models.DecimalField(max_digits=10, decimal_places=1)
    description = models.TextField(max_length=3000)

    class Meta:
        ordering = ['budget']





class Intros(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )
    statement = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=250,
    unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)

    status = models.CharField(max_length=10,
    choices=STATUS_CHOICES,
    default='draft')

         
    def __str__(self):
        return self.statement
