from django.shortcuts import render
from .models import Image, Profile
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    images= Image.objects.all().order_by('-id')
    return render(request, 'all-insta/index.html', {'images':images} )

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    # get images for the current logged in user
    image = Image.objects.filter(user_id=current_user.id)
    # get the profile of the current logged in user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request, 'profile.html', {"image": image, "profile": profile})