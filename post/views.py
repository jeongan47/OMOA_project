from django.shortcuts import render, redirect
from django.db.models.query_utils import Q
from post.models import Post 
from django.urls import reverse
# Create your views here.
    
def ott_choice(request):
    if not request.user.is_authenticated: # 유저의 접근이 올바르지 않다면 로그인 화면으로 보내버려
        return redirect("user:login")

    return render(request,"post/ott_choice.html")

def ott_view(request, ott):
    if not request.user.is_authenticated: # 유저의 접근이 올바르지 않다면 로그인 화면으로 보내버리기
        return redirect("user:login")

    print("ott_view 실행!")
    
    query = request.GET.get("q")
    print("query:", query)

    if query:
        search = Post.objects.filter(content_name__contains = query, content_ott__contains=ott)
    else:
        search = Post.objects.filter(content_ott__contains=ott)
    
    context = {
        "posts": search
    }

    return render(request,"post/post_list.html", context)

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

    return render(request,"post/post_detail.html", context)

def post_search(request):
    query = request.GET.get("q")
    print("query:", query)
    if query:
        search = Post.objects.filter(content_name__contains = query)
    else:
        search = Post.objects.all()
    context = {"content_name": search}
    return render(request, "post/post_list.html", context)

def wish_list(request, post_id):
    wish = Post.objects.get(id = post_id)
    user = request.user

    if user.like_posts.filter(id = wish.id).exists():
        user.like_posts.remove(post)

    else: 
        user.like_posts.add(wish)

    url_next = request.GET.get("next") or reverse("post:") + f"#post-{post.id}"