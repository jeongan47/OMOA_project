from django import forms
from review.models import Review, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "post",
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
            "user",
            "post",
            "title",
            "content",
        ]