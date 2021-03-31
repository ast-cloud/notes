from django.db import models

# Create your models here.


class Notetable(models.Model):
    
    note=models.CharField(max_length=500)
    userid=models.CharField(max_length=200)
    dt=models.DateTimeField()

    def __str__(self):
        return str(self.dt)