from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Post
def index(request):
    posts = Post.objects.all()
    contex = {
        'posts':posts
    }
    return render(request,'blog/index.html',contex)


def post(request,post_id):
    posts = get_object_or_404(Post,pk=post_id)
    contex = {
        'posts':posts
    }
    return render(request,'blog/post_details.html',contex)