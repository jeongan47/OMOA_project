from django.shortcuts import render, redirect
from django.db.models.query_utils import Q
from post.models import Post 
from review.forms import ReviewForm
from django.urls import reverse
from tablib import Dataset
from .xlimport import PostResource
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

    review_form = ReviewForm()
    
    context = {
        "post": post,
        "review_form":review_form,
    }

    return render(request,"post/post_detail.html", context)

def post_detail_like(request, post_id):
    print("like start!")
    post = Post.objects.get(id = post_id)
    user = request.user

    print("post: ", post)
    print("user: ", user)

    # 유저가 찜한 목록에 이미 있다면 목록에서 지우고 없다면 목록에 추가
    user.like_posts.remove(post) if user.like_posts.filter(id = post.id).exists() else user.like_posts.add(post)

    return redirect("post:post_detail", id=post_id)

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

def importExcel(request):
    if not request.user.is_authenticated: # 유저의 접근이 올바르지 않다면 로그인 화면으로 보내버려
        return redirect("user:login")

    if not request.user.is_staff: # 권한이 없는 유저가 접근할 경우
        return redirect("user:login")

    if request.method == 'POST':
        post_resource = PostResource()
        dataset = Dataset()
        new_post = request.FILES['my_file']
        imported_data = dataset.load(new_post.read(), format='xlsx')

        for data in imported_data:
            value = Post(
                content_name = data[0],
                content_description = data[1],
                content_act = data[2],
                content_dir = data[3],
                content_ott = data[4],
                content_genre = data[5],
                post_image = data[6],
                content_year = data[7]
            )
            value.save()

    return render(request, 'post/form.html')