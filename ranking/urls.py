from django.urls import path
from ranking import views

app_name = "ranking"
urlpatterns = [
    path("",views.omoa_home, name = "home"),
    path("ranking/",views.ranking_page, name = "ranking"),
]