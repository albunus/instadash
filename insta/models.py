from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt

# Create your models here.

class Images(models.Model):
    name = models.CharField(max_length=100)
    caption = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image')
    
    def save_image(self):
        self.save()
        
        
    # update image
    def update_image(self, name):
        self.name = name
        self.name = name
        self.save()

    # get all images
    @classmethod
    def get_all_images(cls):
        images = Images.objects.all()
        return images

    
    def delete_image(self):
        self.delete()
    
    def __str__(self):
        return self.name
