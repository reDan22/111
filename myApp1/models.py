from django.db import models

class ComputerBuild(models.Model):
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    cpu = models.CharField(max_length=255)
    gpu = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name