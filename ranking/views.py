from django.shortcuts import render, redirect
from ranking.models import Netflix_movieRank, Netflix_tvRank, Amazon_movieRank, Amazon_tvRank, Disney_Rank, Wavve_movieRank, Wavve_tvRank

# Create your views here.
def omoa_home(request):
    return redirect("ranking:ranking")

def ranking_page(request):

    netflix_movieranks = Netflix_movieRank.objects.all()
    netflix_tvranks = Netflix_tvRank.objects.all()
    amazon_movieranks = Amazon_movieRank.objects.all()
    amazon_tvranks = Amazon_tvRank.objects.all()
    disney_ranks = Disney_Rank.objects.all()
    wavve_movieranks = Wavve_movieRank.objects.all()
    wavve_tvranks = Wavve_tvRank.objects.all()

    context = {
        "netflix_movieranks": netflix_movieranks,
        "netflix_tvranks": netflix_tvranks,
        "amazon_movieranks": amazon_movieranks,
        "amazon_tvranks": amazon_tvranks,
        "disney_ranks": disney_ranks,
        "wavve_movieranks": wavve_movieranks,
        "wavve_tvranks": wavve_tvranks
    }

    return render(request,"ranking/ranking.html",context)