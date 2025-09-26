from django.shortcuts import render, redirect
from review.models import Review
from review.forms import ReviewForm

# Create your views here.
def review_list(request):
    # 모든 글 목록을 템플릿으로 전달
    reviews = Review.objects.all()

    context = {
        "reviews": reviews,
        }
    return render(request,"review/review_list.html", context)

def review_add(request):
    if request.method =="POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            post.save()

            return redirect("review:review_list")


    else:                       
        form = ReviewForm()   
    
    context ={"form": form}
    return render(request,"review/review_add.html", context)