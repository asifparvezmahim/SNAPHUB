from django.shortcuts import render,redirect
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
        