from django.shortcuts import render, redirect
from review.models import Review, Comment
from post.models import Post
from review.forms import ReviewForm, CommentForm    
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden

# Create your views here.
def review_list(request):
    # 모든 글 목록을 템플릿으로 전달
    reviews = Review.objects.all()

    context = {
        "reviews": reviews,
        }
    return render(request,"review/review_list.html",context)

def review_add(request, post_id):
    post = Post.objects.get(pk=post_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit = False)
            review.user = request.user
            review.post_id = post_id    
            review.save()
            return redirect("review:review_list")
    else:
        form = ReviewForm()

    context = {
        "form":form,
        "post":post,
    }

    return render(request, 'review/review_add.html',context)

def review_detail(request,review_id):
    comment_form = CommentForm()
    
    review = Review.objects.get(pk=review_id)
    context = {
        "review":review,
        "comment_form":comment_form,
    }
    return render(request,"review/review_detail.html",context)

@require_POST
def comment_add(request):
    form = CommentForm(data = request.POST)

    if form.is_valid():
        # commit = False 옵션으로 메모리상에 Comment 객체 생성
        comment = form.save(commit = False)
        comment.user = request.user
        comment.save()

        return redirect("review:review_detail",comment.review.id)

    return redirect('review:review_list')
    
@require_POST
def comment_delete(request, comment_id):
    comment = Comment.objects.get(pk = comment_id)
    if comment.user == request.user:
        comment.delete()
        return redirect("review:review_detail",comment.review.id) 
    
    else:
        return HttpResponseForbidden("이 댓글을 삭제할 권한이 없습니다")