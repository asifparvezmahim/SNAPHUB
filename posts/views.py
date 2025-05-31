from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.models import Post
# from .models import Post
from .forms import PostForm

# Create your views here.
def add_post(request):
    if request.method == "POST":
        post_form = PostForm(request.POST,request.FILES)
        if post_form.is_valid():
            post=post_form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect("add_post")
    else:
        post_form = PostForm()
    return render(request,"add_posts.html",{"form":post_form})


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        messages.error(request, "You are not allowed to edit this post.")
        return redirect('profile')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully.")
            return redirect('profile')
    else:
        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request,post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user:
        messages.error(request, "You are not authorized to delete this post.")
        return redirect('profile')

    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted successfully.")
        return redirect('profile')

    return render(request, 'confirm_delete.html', {'post': post})
