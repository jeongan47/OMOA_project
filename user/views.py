from django.shortcuts import render, redirect, get_object_or_404
from user.forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from user.models import User
from django.urls import reverse



# Create your views here.
def login_view(request):
    # 이미 로그인되어 있다면
    if request.user.is_authenticated:
        return redirect('post:ott_view', "all")
    
    if request.method == "POST":
        # LoginForm 객체를 만들며, 입력 데이터는 request.POST 를 사용
        form = LoginForm(data = request.POST)

        # LoginForm 에 전달된 데이터가 유효하다면
        if form.is_valid():
            # username과 password 값을 가져와 변수에 할당
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # username, password에 해당하는 사용자가 있는지 검사
            user = authenticate(username = username, password = password)

            # 해당 사용자가 존재한다면
            if user:
                # 로그인 처리 후, 피드 페이지로 redirect
                login(request, user)
                return redirect('post:ott_view', "all")
            
            else:
                # 사용자가 없다면 form에 에러 추가
                form.add_error(None, "입력한 자격증명에 해당하는 사용자가 없습니다")

    else:
        # LoginForm 객체를 생성
        form = LoginForm()

    # 생성한 LoginForm 객체를 템플릿에 "form" 이라는 키로 전달
    context = {
        "form": form,
    }
    return render(request, "user/login.html", context)

def logout_view(request):
    # logout 함수 호출에 request를 전달
    logout(request)

    # logout 처리 후, 로그인 페이지로 이동
    return redirect("user:login")

def signup(request):
    if request.method == "POST":
        form = SignupForm(data = request.POST, files = request.FILES)

        if form.is_valid():
            # Form에 에러가 없다면 form의 save() 메서드로 사용자를 생성
            user = form.save()
            login(request, user)
            return redirect('post:ott_view', "all")

    else: # GET 요청에서는 빈 form 을 보여줌
        # SignupForm 인스턴스를 생성, Template에 전달
        form = SignupForm()

    # context로 전달되는 form은 두 가지 경우가 존재
    # 1. POST 요청에서 생성된 form 이 유효하지 않은 경우 -> 에러를 포함한 form이 사용자에게 보여짐
    # 2. GET 요청으로 빈 form 이 생성된 경우 -> 빈 form이 사용자에게 보여짐
    context = {
        "form": form
    }
    return render(request, "user/signup.html", context)

def followers(request, user_id):
    user = get_object_or_404(User, id=user_id)
    relationships = user.follower_relationships.all()
    context = {
        "user":user,
        "title":"Followers",
        "relationships":relationships,
    }
    return render(request,"user/followers.html", context)

def following(request, user_id):
    user = get_object_or_404(User, id=user_id)
    relationships = user.following_relationships.all()
    context = {
        "user":user,
        "title":"Following",
        "relationships":relationships,
    }
    return render(request,"user/following.html", context)

def follow(request, user_id):
    # 로그인한 유저
    user = request.user

    # 팔로우 하려는 유저
    target_user = get_object_or_404(User, id= user_id)

    # 팔로우 하려는 유저가 이미 자신의 팔로잉 목록에 있는 경우
    if target_user in user.following.all():
        # 팔로잉 목록에서 제거
        user.following.remove(target_user)
    # 팔로우 하려는 유저가 자신의 팔로잉 목록에 없는 경우
    else:
        # 팔로잉 목록에 추가
        user.following.add(target_user)
    
    # 팔로우 토글 후 이동할 URL이 전달되었다면 해당 주소로,
    # 전달되지 않았다면 로그인 한 유저의 프로필 페이지로 이동
    url_next = request.GET.get("next") or reverse("user:profile", args=[user.id])
    return redirect(url_next)

def my_page(request, id):
    pageuser = User.objects.get(id = id)
    context = {"pageuser": pageuser}

    return render(request, "user/profile.html", context)

def user_follow(request, id):
    print("follow start!")
    follow_user = User.objects.get(id = id)
    user = request.user

    # 유저가 찜한 목록에 이미 있다면 목록에서 지우고 없다면 목록에 추가
    # user.like_posts.remove(post) if user.like_posts.filter(id = post.id).exists() else user.like_posts.add(post)
    user.following.remove(follow_user) if follow_user in user.following.all() else user.following.add(follow_user)

    return redirect("user:mypage", id=id)

def my_likelist(request, id):
    user = User.objects.get(id = id)
    me = request.user
    context = {
        "user": user,
        "me": me,
        }

    return render(request, "user/mylike.html", context)

def my_reviewlist(request, id):
    user = User.objects.get(id = id)

    context = {"user": user}

    return render(request, "user/myreview.html", context)

def my_followlist(request, id):
    user = User.objects.get(id = id)

    context = {"user": user}

    return render(request, "user/myfollow.html", context)
