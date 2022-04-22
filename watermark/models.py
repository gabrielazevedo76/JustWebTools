from contextlib import nullcontext
from email.policy import default
from django.core.files.storage import FileSystemStorage
from django.db import models

# Create your models here.

class WatermarkModel(models.Model):

    width = models.BigIntegerField(null=True, default=0)
    height = models.BigIntegerField(null=True, default=0)
    img = models.ImageField(upload_to='watermark/media/img/', blank=True, default='')
    logo = models.ImageField(upload_to='watermark/media/logo/', blank=True, default='')
    watermarked = models.ImageField(default='')

    def __str__(self):
        return str(self.id)
