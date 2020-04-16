from django.shortcuts import render
from django.views import generic
from .models import Post
from django.views.generic.list import ListView

class PostList(generic.ListView):
    queryset = Post.objects.all().order_by('-created_on')
    template_name = 'index.html'


class PostGallery(ListView):
    model = Post
    queryset = Post.objects.order_by('-id')
    template_name = 'gallery.html'
    context_object_name = 'post_list'




class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')