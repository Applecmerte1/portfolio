from django.db import models

class Blog_project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date = models.DateField()