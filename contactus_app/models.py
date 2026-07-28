from django.db import models


class Footer(models.Model):
    post_address = models.CharField(max_length=120)
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    whatsapp = models.CharField(max_length=120, null=True, blank=True)
    telegram = models.CharField(max_length=120, null=True, blank=True)
    instagram = models.CharField(max_length=120, null=True, blank=True)

class Message(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=120, null=True, blank=True)
    body = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
