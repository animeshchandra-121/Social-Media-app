from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comments, Profile
from .form import PostForm, CommentForm, ProfileForm
from django.urls import reverse
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit= False)
            post.author = request.user
            post.save()
            return redirect('social:post')
    context = {'posts':posts, 'form': form}
    return render(request, 'post.html', context= context)

def postdetailview(request, id):
    post = Post.objects.get(id= id)
    comment_object = Comments.objects.filter(post = post)
    comment = CommentForm()
    if request.method == "POST":
        comment = CommentForm(request.POST)
        if comment.is_valid():
            com =  comment.save(commit= False)
            com.post = post
            com.users = request.user
            com.save()
            return redirect('social:post-detail', id = post.id)
            
    context = {
        'post':post,
        'comment':comment,
        'comment_obj':comment_object
    }
    return render(request, "post_detail.html", context= context)

def update_post(request, id):
    post = Post.objects.get(id= id)
    form = PostForm(instance= post)
    if request.method == "POST":
        form = PostForm(request.POST, instance= post)
        if form.is_valid():
            posts = form.save(commit= False)
            posts.author = request.user
            posts.save()
            return redirect(reverse('social:post-detail', kwargs={'id': post.id}))
    
    context = {'post': post,'form':form}
    
    return render(request, 'update_post.html', context= context)

def delete_post(request, id):
    post = Post.objects.get(id= id)
    if request.method == "POST":
        post.delete()
        return redirect('social:post')
    context= {"post":post}
    return render(request, 'delete.html', context=context)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

def profile_view(request, id):
    profile = Profile.objects.filter(user_id=id).first()
    user = profile.user
    if not profile:
        return render(request, "profile_not_found.html")  # Create a template for missing profiles
    post = Post.objects.all()
    
    followers = profile.followers.all()
    is_following = False
    for follower in followers:
        if follower == request.user:
            is_following = True
            break
        else:
            is_following = False
    number_of_followers = len(followers)
    context= {"posts": post,
              "user": user,
              "profile": profile,
              "number_of_followers": number_of_followers,
              "is_following": is_following}
    
    return render(request, 'profile_setup.html', context= context)

def edit_profile(request, id):
    profile = get_object_or_404(Profile, user_id=id)
    form = ProfileForm(instance= profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance= profile)
        if form.is_valid():
            pro = form.save(commit= False)
            pro.user= request.user
            pro.save()
            return redirect(reverse('social:profile', kwargs={'id': profile.user.id}))
    
    context = {'post': profile,'form':form}
    
    return render(request, 'update_profile.html', context= context)

def addFollower(request, id):
    profile = get_object_or_404(Profile, user_id=id)
    profile.followers.add(request.user)
    return redirect(reverse('social:profile', kwargs={'id': profile.user.id}))

def removeFollower(request, id):
    profile = get_object_or_404(Profile, user_id = id)
    profile.followers.remove(request.user)
    return redirect(reverse('social:profile', kwargs={'id':profile.user.id}))

def addlikes(request, id):
    post = Post.objects.get(id = id)

    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        post.dislikes.remove(request.user)
    
    return redirect('social:post')

def removelikes(request, id):
    post = Post.objects.get(id = id)
    if post.dislikes.filter(id = request.user.id).exists():
        post.dislikes.remove(request.user)
    else:
        post.dislikes.add(request.user)
        post.likes.remove(request.user)
    
    return redirect('social:post')

def search_bar(request):
    query = request.GET.get('query')
    profile_list = Profile.objects.filter(
        Q(user__username__icontains= query)
    )

    context= {
        "profile_list": profile_list
    }

    return render(request, 'search.html', context=context)