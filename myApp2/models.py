from django.db import models

class StudentInfo2(models.Model):
    title = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    all_info = models.CharField(max_length=255)
    img = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name