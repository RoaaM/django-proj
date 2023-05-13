from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    text = models.TextField(null=True)
