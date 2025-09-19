from django.urls import path
from post import views

app_name = "post"

urlpatterns = [
    path("ott_choice/",views.ott_choice, name = "choice"),
]