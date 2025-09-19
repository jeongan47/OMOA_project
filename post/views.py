from django.shortcuts import render, redirect

# Create your views here.
def ott_choice(request):
    if not request.user.is_authenticated: # 유저의 접근이 올바르지 않다면 로그인 화면으로 보내버려
        return redirect("user:login")

    return render(request,"ott_choice.html") 