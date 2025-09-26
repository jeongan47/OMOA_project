from django.shortcuts import render, redirect
from django.db.models.query_utils import Q
from post.models import Post 
from review.forms import ReviewForm
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
    review_form = ReviewForm()
    
    context = {
        "post": post,
        "review_form":review_form,
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

def my_list(request, post_id):
    my = Post.objects.get(id = post_id)
    user = request.user
# 사용자가 "좋아요를 누른 Post 목록"에 "좋아요 버튼을 누른 Post"가 존재한다면
    if user.like_posts.filter(id = my.id).exists():
       # My 목록에서 삭제
       user.like_posts.remove(my)

     # 존재하지 않는다면 My 목록에 추가
    else: 
        user.like_posts.add(my)
 # next로 값이 전달되었다면 해당 위치로, 전달되지 않았다면 피드페이지에서 해당 Post위치로 이동
    url_next = request.GET.get("next") or reverse("post:") + f"#post-{my.id}"

    return redirect(url_next)