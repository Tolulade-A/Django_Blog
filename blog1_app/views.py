from django.shortcuts import render
from .models import Blog1

# Create your views here.
def index(request):
    blogs = Blog1.objects.all()
    return render(request, 'index.html', {'blogs': blogs})

def blog(request, pk):
    blogs = Blog1.objects.get(id=pk) #blog1 is the class
    return render(request, 'blog.html', {'blogs': blogs})


