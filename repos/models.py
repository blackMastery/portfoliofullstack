from django.db import models



class Repo(models.Model):

    url = models.URLField(max_length=500)
    description = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['name']

    