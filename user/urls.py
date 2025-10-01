from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from user import views

app_name = "user"
urlpatterns = [
    path("login/", views.login_view, name = "login"),
    path("logout/", views.logout_view, name = "logout"),
    path("signup/", views.signup, name = "signup"),
    path("my_page/<int:id>/", views.my_page, name = "mypage"),
    path("my_page/<int:id>/follow/", views.user_follow, name = "userfollow"),
    path("my_page/<int:id>/mylike/", views.my_likelist, name= "mylike"),
    path("my_page/<int:id>/myreview/", views.my_reviewlist, name= "myreview"),
    path("my_page/<int:id>/myfollow/", views.my_followlist, name= "myfollow"),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)