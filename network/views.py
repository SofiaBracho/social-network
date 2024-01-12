from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
import json

from .models import User, Post, PostLikes, UserFollowing


def index(request):
    posts_list = Post.objects.order_by('-posted_on')
    paginator = Paginator(posts_list, 10) # Show 10 posts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "network/index.html", {
        'page_obj': page_obj
    })


@login_required
def following(request):
    # Get a list of following users
    following_users = [uf.following_user for uf in request.user.following.all()]

    posts_list = Post.objects.filter(posted_by__in=following_users).order_by('-posted_on')
    paginator = Paginator(posts_list, 10) # Show 10 posts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "network/following.html", {
        'page_obj': page_obj
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


@login_required
def post(request):
    # If the user sends the form
    if request.method == "POST":
        # get content
        content = request.POST["content"]

        # create the new post
        Post.objects.create(content=content, posted_by=request.user)

        # redirect the page      
        return HttpResponseRedirect('/')
    
    return HttpResponseRedirect('/')


@login_required
def post_edit(request):
    #the request method is checked to make sure it is a POST request
    if request.method == "POST":
        #the request body is accessed using request.body, which contains the raw request payload
        data = request.body
        # data is a bytes-like object, so you might want to convert it to a dictionary or a string
        data = data.decode('utf-8')
        # parse the JSON data
        data = json.loads(data)
        # now you can access the data as a dictionary
        post_id = data['post_id']
        new_content = data['content']

        post_to_edit = Post.objects.get(pk=post_id)
        
        # checks that the user owns this post
        if not (post_to_edit.posted_by == request.user):
            return JsonResponse({'error':'You do not have permission to edit this post.'}, status=403)
        
        post_to_edit.content = new_content
        post_to_edit.save()

        print(new_content)
        return JsonResponse({'result': 'success'},safe=False)
        
    else:
        return JsonResponse({'error': 'Bad request'}, status=400)


def profile(request, user_id):
    # Get the requested user
    user_profile = User.objects.get(pk=user_id)

    # Get info about the following status
    if request.user.is_authenticated:
        following = UserFollowing.objects.filter(user=request.user, following_user=user_profile) 
    else:
        following = False

    posts_list = Post.objects.filter(posted_by=user_profile).order_by('-posted_on')
    paginator = Paginator(posts_list, 10) # Show 10 posts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Return user info and posts
    return render(request, "network/profile.html", {
        'user_profile': user_profile,
        'following': following,
        'page_obj': page_obj
    })


@login_required
def follow(request):
    #the request method is checked to make sure it is a POST request
    if request.method == "POST":
        #the request body is accessed using request.body, which contains the raw request payload
        data = request.body
        # data is a bytes-like object, so you might want to convert it to a dictionary or a string
        data = data.decode('utf-8')
        # parse the JSON data
        data = json.loads(data)
         # now you can access the data as a dictionary
        action = data['action']
        user_id = data['user_id']
        following_user = User.objects.get(pk=user_id)

        if action == "follow":
            UserFollowing.objects.create(user=request.user, following_user=following_user)
            return JsonResponse({'message': f'You are following {following_user.username} now', 'result': 'success'},safe=False)
        elif action == "unfollow":
            UserFollowing.objects.filter(user=request.user, following_user=following_user).delete()
            return JsonResponse({'message': f'You stoped following {following_user.username}', 'result': 'success'},safe=False)
        
    else:
        return JsonResponse({'error': 'Bad request'}, status=400)
    

@login_required
def like(request):
    #the request method is checked to make sure it is a POST request
    if request.method == "POST":
        #the request body is accessed using request.body, which contains the raw request payload
        data = request.body
        # data is a bytes-like object, so you might want to convert it to a dictionary or a string
        data = data.decode('utf-8')
        # parse the JSON data
        data = json.loads(data)
         # now you can access the data as a dictionary
        is_liked = data['is_liked']
        post_id = data['post_id']
        post_liking = Post.objects.get(pk=post_id)

        if is_liked == 'True':
            PostLikes.objects.filter(user=request.user, post=post_id).delete()
            return JsonResponse({'message': f'You stopped liking {post_liking.posted_by}\'s post', 'result': 'success'},safe=False)
        elif is_liked == 'False':
            PostLikes.objects.create(user=request.user, post=post_liking)
            return JsonResponse({'message': f'You like {post_liking.posted_by}\'s post', 'result': 'success'},safe=False)
        
    else:
        return JsonResponse({'error': 'Bad request'}, status=400)