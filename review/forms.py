from django import forms
from review.models import Review, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "review",
            "content",
        ]
        widgets = {
            "content": forms.Textarea(
                attrs = {
                    "placeholder": "댓글 달기...",
                }
            )
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields =[
            "title",
            "content",
        ]
        widgets = {
            "content": forms.Textarea(
                attrs = {
                    "placeholder":"내용을 입력해주세요",
                }
            )
        }