from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Post_vedio
# Create your views here.


def home(request):
    last_vedio = Post_vedio.objects.all().order_by("-id")[0]
    return render(request,'home.html',{'last_vedio':last_vedio})



