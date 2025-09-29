from django.urls import path
from post import views

app_name = "post"
urlpatterns = [
    path("ott_choice/",views.ott_choice, name = "choice"),
    path("ott/<str:ott>/", views.ott_view, name= "ott_view"),
    path("post_detail/<int:id>/", views.post_detail, name= "post_detail"),
    path("post_detail/<int:post_id>/like/", views.post_detail_like, name= "post_detail_like"),
    path("import/", views.importExcel, name= "importExcel"),
]