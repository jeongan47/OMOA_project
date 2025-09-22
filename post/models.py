from django.db import models

# Create your models here.
class Post(models.Model):
    content_name = models.CharField("작품제목",max_length=50)
    content_description = models.TextField("시놉시스",blank=True)
    content_act = models.CharField("출연진")
    content_dir = models.CharField("감독")
    content_ott = models.CharField("OTT")
    content_genre = models.CharField("장르")
    post_image = models.ImageField("포스터")