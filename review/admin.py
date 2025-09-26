from django.contrib import admin
from review.models import Comment,Review


# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "content",
        "title",
        "post",
        "created",
    ]
    inlines = [
        CommentInline,
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "review",
        "content",
        "created",
    ]