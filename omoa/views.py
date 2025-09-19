from django.shortcuts import render, redirect

def index(request):  #만약 유저의 접근이 올바르면 OTT띄우는 창으로 보내버려
    if  request.user.is_authenticated:
        return redirect("post:ott_choice")
    
    else: # 유저의 접근이 올바르지 않다면 다시 로그인 화면으로 보내버려
        return redirect("user/login")