from django.shortcuts import render
from .models import Images

# Create your views here.
def index(request):
    images= Images.objects.all().order_by('-id')
    return render(request, 'index.html', {'images':images} )