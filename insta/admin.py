from django.contrib import admin
from .models import Images, Profile, Likes, Comments

# Register your models here.
admin.site.register(Images)
admin.site.register(Profile)
admin.site.register(Likes)
admin.site.register(Comments)
