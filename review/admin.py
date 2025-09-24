from django.contrib import admin
from review.models import Review
from post.models import Post

# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "content",
        "title",
        "post",
    ]