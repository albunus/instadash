from django.shortcuts import render
from .models import Images
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/account/register/')
def index(request):
    images= Images.objects.all().order_by('-id')
    return render(request, 'all-insta/index.html', {'images':images} )