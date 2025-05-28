from django.db import models
from django.core.validators import MinLengthValidator

class MineInfo2(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class ProgramInfo2(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    program_url = models.URLField()
    
    # Руководство программы
    head_name = models.CharField(max_length=100)
    head_image = models.CharField(max_length=100)
    head_email = models.EmailField()
    
    # Менеджер программы
    manager_name = models.CharField(max_length=100)
    manager_image = models.CharField(max_length=100)
    manager_email = models.EmailField()

    def __str__(self):
        return self.title

class CourseMateInfo2(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField()
    email = models.EmailField()
    number = models.CharField(max_length=20)
    program = models.ForeignKey(ProgramInfo2, on_delete=models.CASCADE, related_name='mates')

    def __str__(self):
        return self.name

class StudentInfo2(models.Model):
    title = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    all_info = models.CharField(max_length=255)
    img = models.CharField(max_length=100)

    def __str__(self):
        return self.title
