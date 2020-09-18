from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    return render(request, 'index.html')

"""
def press(request, pk):
    post = Post.objects.all().order_by('-date_posted')

    context = {'Post':post}
    return render(request, 'press.html', context)
"""

# Class Based view
class PostView(ListView):
    model = Post
    template_name = 'press.html'
    context_object_name = 'Post'
    ordering = ['-date_posted']


class DetailPost(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'posts'

class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    context_object_name = 'posts'
    success_url = '/press'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'about.html')
