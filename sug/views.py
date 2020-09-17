from django.shortcuts import render
from .models import Post

def index(request):
    return render(request, 'index.html')

def press(request, pk):
    post = Post.objects.all().order_by('-date_posted')

    context = {'Post':post}
    return render(request, 'press.html', context)

def about(request):
    return render(request, 'about.html')
