from django.urls import path
from user import views

app_name = "user"
urlpatterns = [
    path("login/", views.login_view, name = "login"),
    path("logout/", views.logout_view, name = "logout"),
    path("signup/", views.signup, name = "signup"),
    path("<int:user_id>/followers/",views.followers, name = "followers"),
    path("<int:user_id>/following/", views.following, name = "following"),
    path("<int:user_id>/follow/",views.follow, name="follow"),
    path("my_page/<int:id>/", views.my_page, name = "mypage"),
    ]