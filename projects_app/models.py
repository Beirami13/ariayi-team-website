from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    address = models.CharField(max_length=120)
    image = models.ImageField(upload_to='project')

    def __str__(self):
        return self.title

