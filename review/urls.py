from django.urls import path
from review import views

app_name = "review"
urlpatterns = [
    path("",views.review_list, name = "review_list"),
    path("add/<int:post_id>/",views.review_add, name = "review_add"),
    path("delete/<int:review_id>/",views.review_delete, name = "review_delete"),
    path("<int:review_id>/",views.review_detail, name= "review_detail"),
    path("comment_add/", views.comment_add, name="comment_add"),
    path("comment_delete/<int:comment_id>/", views.comment_delete, name="comment_delete"),
]