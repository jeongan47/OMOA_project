from django.shortcuts import render, redirect
from post.models import Post 

# Create your views here.
def ott_choice(request):
    if not request.user.is_authenticated: # 유저의 접근이 올바르지 않다면 로그인 화면으로 보내버려
        return redirect("user:login")

    return render(request,"post/ott_choice.html")

def netflix(request):
    netflix = Post.objects.filter(content_ott = "Netflix")
    context = {
        "netflix": netflix
    }
    return render(request,"post/netflix.html",context)

def amazon(request):
    amazon = Post.objects.filter(content_ott = "Amazon Prime Video")
    context = {
        "amazon": amazon
    }
    return render(request,"post/amazon.html",context)

def disney(request):
    disney = Post.objects.filter(content_ott = "Disney Plus")
    context = {
        "disney": disney
    }
    return render(request,"post/disney.html",context)

def wavve(request):
    wavve = Post.objects.filter(content_ott = "wavve")
    context = {
        "wavve": wavve
    }
    return render(request,"post/wavve.html",context)