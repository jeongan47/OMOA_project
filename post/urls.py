from django.urls import path
from post import views

app_name = "post"
urlpatterns = [
    path("ott_choice/",views.ott_choice, name = "choice"),
    path("netflix/",views.netflix, name = "netflix"),
    path("amazon/", views.amazon, name = "amazon"),
    path("disney/", views.disney, name = "disney"),
    path("wavve/", views.wavve, name = "wavve"),
]