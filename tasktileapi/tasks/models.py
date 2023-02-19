from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    order = models.IntegerField()
    description = models.TextField()
    type = models.CharField(max_length=20)
    tile = models.ForeignKey('Tile', on_delete=models.CASCADE)

class Tile(models.Model):
    launch_date = models.DateTimeField()
    status = models.CharField(max_length=20)
