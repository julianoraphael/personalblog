from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound

def list_posts(request):
    posts = Post.objects.order_by('-publication_date')
    return render(request, 'blog/list_posts.html', {'posts': posts})

def detail_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/detail_post.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_posts')
    else:
        form = PostForm()
    
    return render(request, 'blog/create_post.html', {'form': form})

@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('list_posts')
    else:
        form = PostForm()
    
    return render(request, 'blog/create_post.html', {'form': form})

def page_not_found(request, exception):
    return HttpResponseNotFound(render(request, 'blog/error.html', status=404))
