from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import BlogPost, UserProfile


# Create your views here.
class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blog/blogpost_list.html"
    context_object_name = "posts"
    ordering = ["-last_edited_at"]


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blog/blogpost_detail.html"
    context_object_name = "post"


# class BlogPostCreateView(CreateView):
#     model = BlogPost
#     template_name = 'blog/blogpost_form.html'
#     form_class = BlogPostForm
#     success_url =

# class BlogPostUpdateView(UpdateView):
#     model = BlogPost
#     template_name = 'blog/blogpost_form.html'
#     context_object_name = 'post'
#     form_class = BlogPostForm
#     success_url =

# class BlogPostDeleteView(DeleteView):
#     model = BlogPost
#     template_name = 'blog/blogpost_confirm_delete.html'
#     context_object_name = 'post'
#     success_url =
