from django.shortcuts import render
from review.models import Review
# Create your views here.
def review_list(request):
    reviews = Review.objects.filter()
    context = {
        "reviews":reviews
    }
    return render(request, "review_list.html", context)
