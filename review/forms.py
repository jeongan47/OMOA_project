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
                    "class":"form-control",
                    "rows":"3",
                    "style": "resize: none; width:90%; margin-right: 15px;",
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
            "title": forms.TextInput(
                attrs= {
                    "placeholder":"제목을 입력해주세요", "class":"form-control", "aria-describedby": "inputGroup-sizing-default", "style":"width:80%"
                }
            ),
            "content": forms.Textarea(
                attrs = {
                    "placeholder":"내용을 입력해주세요", "class":"form-control"
                }
            )
        }