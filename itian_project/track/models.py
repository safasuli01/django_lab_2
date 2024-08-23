from django.db import models


# Create your models here.
class Track(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    description = models.TextField()
