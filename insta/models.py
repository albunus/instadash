from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt

# Create your models here.

class Images(models.Model):
    name = models.CharField(max_length=100)
    caption = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image')
    
    def __str__(self):
        return self.pic_name
