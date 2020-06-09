from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
from .models import Post

class BlogList(ListView):
    model = Post 
    template_name = 'blog/index.html'

# def index(request):
#     posts = Post.objects.all()
#     contex = {
#         'posts':posts
#     }
#     return render(request,'blog/index.html',contex)


# def post(request,post_id):
#     posts = get_object_or_404(Post,Post.pk)
#     contex = {
#         'posts':posts
#     }
#     return render(request,'blog/post_details.html',contex)

class Blogdetails(DetailView):
    model = Post 
    template_name = 'blog/post_details.html'
    # contex_object-name = 'indiv_post'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/new_post.html'
    fields = '__all__'

class BlogUpdate(UpdateView):
    model = Post
    template_name = 'blog/edit_post.html'
    fields  = ['title','body']


class BlogDelete(DeleteView):
    model = Post 
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('index')