from django import forms
from post.models import Post
from review.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "user",
            "post",
            "content",
        ]
        

class PostForm(forms.Form):
    class meta:
        model = Post
        fields = '__all__'