from django.urls import path
from post import views

app_name = "post"
urlpatterns = [
    path("ott_choice/",views.ott_choice, name = "choice"),
    path("<str:ott>/", views.ott_view, name= "ott_view"),
    path("post_detail/<int:id>/", views.post_detail, name= "post_detail"),
]