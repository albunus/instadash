from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.

class Images(models.Model):
    name = models.CharField(max_length=50)
    caption = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image')
    profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    
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
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = CloudinaryField('image')
    bio = models.TextField(max_length=500, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)

    def update(self):
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
        
class Likes(models.Model):
    image = models.ForeignKey(Images, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.likes

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Images, on_delete=models.CASCADE)
    comment = models.CharField(max_length=50)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

