from django.db import models

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey("user.User",
                             verbose_name = "작성자",
                             on_delete = models.CASCADE)
    post = models.ForeignKey("post.Post",
                             verbose_name="작품명",
                             on_delete=models.CASCADE)
    content = models.TextField("내용")
    created = models.DateTimeField("작성일시", auto_now_add = True)
    title = models.CharField("제목")

    def __str__(self):
        return f"{self.user.id}의 게시글(id: {self.id})"
    

class Comment(models.Model):
    user = models.ForeignKey("user.User",
                             verbose_name="작성자",
                             on_delete=models.CASCADE)
    review = models.ForeignKey("review.Review", verbose_name = "게시글", on_delete = models.CASCADE)
    content = models.TextField("내용")
    created = models.DateTimeField("작성일시", auto_now_add= True)