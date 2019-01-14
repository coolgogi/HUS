from django.shortcuts import render, get_object_or_404
from .forms import PostModelForm
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    TemplateView
)
from .models import Post
from django.urls import reverse
from django.core import serializers 

class PostListView(ListView):
    template_name = 'Potato/post_list.html'
    queryset = Post.objects.all().order_by('-pk')

class PostDetailView(DetailView):
    template_name = 'Potato/post_detail.html'
    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Post, id=id_)

class PostCreateView(CreateView):
    template_name = 'Potato/post_create.html'
    form_class = PostModelForm

class PostUpdateView(UpdateView):
    template_name = 'Potato/post_create.html'
    form_class = PostModelForm
    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Post, id=id_)

class PostDeleteView(DeleteView):
    template_name = 'Potato/post_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Post, id=id_)

    def get_success_url(self):
        return reverse('Potato:postList')