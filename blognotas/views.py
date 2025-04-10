from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404


# Create your views here.
def post_list(request):
    posts = Post.published.all()
    return render(request,'blog/post/list.html',
                  {'posts':posts})

# Segunda vista para mostar un solo de los post


def post_detail(request, id):
    try:
        post = Post.published.get(id=id)

    except Post.DoesNotExist:
        raise Http404("No Post fue encontrado en este caso.")
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})

