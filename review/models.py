from django.db import models

# Create your models here.
class Review(models.Model): #댓글
    user = models.ForeignKey("user.User", verbose_name = "작성자", on_delete = models.CASCADE)
    content = models.TextField("내용", blank = True)

class Comment(models.Model): # 대댓글
    user = models.ForeignKey("user.User",
                             verbose_name = "작성자",
                             on_delete = models.CASCADE)
    post = models.ForeignKey(Review,
                             verbose_name = "포스트",
                             on_delete = models.CASCADE)
    content = models.TextField("내용")
    created = models.DateTimeField("작성일시", auto_now_add = True)