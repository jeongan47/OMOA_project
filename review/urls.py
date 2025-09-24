from django.urls import path
from review import views

app_name = "review"
urlpatterns = [
    path("",views.review_list, name = "review_list"),
    path("add/",views.review_add, name = "review_add"),
]