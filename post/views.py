from django.shortcuts import render, redirect
from post.models import Post 

# Create your views here.
    
def ott_choice(request):
    if not request.user.is_authenticated: # 유저의 접근이 올바르지 않다면 로그인 화면으로 보내버려
        return redirect("user:login")

    return render(request,"post/ott_choice.html")

def netflix(request):
    if not request.user.is_authenticated: # 유저의 접근이 올바르지 않다면 로그인 화면으로 보내버리기
        return redirect("user:login")
    posts = Post.objects.filter(content_ott__contains="Netflix")
    context = {
        "posts": posts
    }
    return render(request,"post/post_list.html",context)

def amazon(request):
    if not request.user.is_authenticated: # 유저의 접근이 올바르지 않다면 로그인 화면으로 보내버리기
        return redirect("user:login")
    posts = Post.objects.filter(content_ott__contains="Amazon")
    context = {
        "posts": posts
    }
    return render(request,"post/post_list.html",context)

def disney(request):
    if not request.user.is_authenticated: # 유저의 접근이 올바르지 않다면 로그인 화면으로 보내버리기
        return redirect("user:login")
    posts = Post.objects.filter(content_ott__contains="Disney Plus")
    context = {
        "posts": posts
    }
    return render(request,"post/post_list.html",context)

def wavve(request):
    if not request.user.is_authenticated: # 유저의 접근이 올바르지 않다면 로그인 화면으로 보내버리기
        return redirect("user:login")
    posts = Post.objects.filter(content_ott__contains="wavve")
    context = {
        "posts": posts
    }
    return render(request,"post/post_list.html",context)