from django.shortcuts import render, redirect
from review.models import Review, Comment
from review.forms import ReviewForm, CommentForm    
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden
from django.urls import reverse

# Create your views here.
def review_list(request):
    # 모든 글 목록을 템플릿으로 전달
    reviews = Review.objects.all()

    context = {
        "reviews": reviews,
        }
    return render(request,"review/review_list.html",context)

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
    return render(request,"review/review_add.html",context)

def review_detail(request,review_id):
    reviews = Review.objects.get(pk=review_id)
    context = {
        "reviews":reviews,
    }
    return render(request,"review/review_detail.html",context)

@require_POST
def comment_add(request):
    form = CommentForm(data = request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()

        if request.GET.get("next"):
            url_next = request.GET.get("next")

        else:
            url_next = reverse("review:review_list") + f"#review-{comment.review.id}"

        return redirect(url_next)
    
@require_POST
def comment_delete(request, comment_id):
    comment = Comment.objects.get(pk = comment_id)
    if comment.user == request.user:
        comment.delete()
        return redirect(f"/review/#review-{comment.review.id}")
    
    else:
        return HttpResponseForbidden("이 댓글을 삭제할 권한이 없습니다")