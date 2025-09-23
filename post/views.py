from django.shortcuts import render, redirect
from post.models import Post 

# Create your views here.
    
def ott_choice(request):
    if not request.user.is_authenticated: # 유저의 접근이 올바르지 않다면 로그인 화면으로 보내버려
        return redirect("user:login")

    return render(request,"post/ott_choice.html")

def ott_view(request, ott):
    if not request.user.is_authenticated: # 유저의 접근이 올바르지 않다면 로그인 화면으로 보내버리기
        return redirect("user:login")

    posts = Post.objects.filter(content_ott__contains=ott)
    context = {
        "posts": posts
    }

    return render(request,"post/post_list.html",context)

def post_detail(request, id):
    if not request.user.is_authenticated: # 유저의 접근이 올바르지 않다면 로그인 화면으로 보내버리기
        return redirect("user:login")
    
    post = Post.objects.get(id = id)

    content_dir_list = eval(post.content_dir)
    post.content_dir = []

    for i in content_dir_list:
        post.content_dir.append(i.strip(',').strip())
    
    content_genre_list = eval(post.content_genre)
    post.content_genre = []

    for i in content_genre_list:
        post.content_genre.append(i.strip())

    post.content_ott = eval(post.content_ott)

    context = {
        "post": post
    }

    return render(request,"post/post_detail.html",context)