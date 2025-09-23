from django.db import models

# Create your models here.
class Post(models.Model):
    content_name = models.CharField("작품제목",max_length=50,blank=True, null=True)
    content_description = models.TextField("시놉시스",blank=True,null=True)
    content_act = models.CharField("출연진",blank=True,null=True)
    content_dir = models.CharField("감독",blank=True,null=True)
    content_ott = models.CharField("OTT", blank=True,null=True)
    content_genre = models.CharField("장르", blank=True,null=True)
    post_image = models.ImageField("포스터", blank=True,null=True)
    content_year = models.CharField("개봉년도", max_length=4, blank=True,null=True)