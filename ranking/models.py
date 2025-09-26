from django.db import models

# Create your models here.
class Last_update(models.Model):
    last_date = models.DateField("날짜", auto_now_add=True)

class Netflix_movieRank(models.Model):
    content_rank = models.CharField("순위",max_length=5)
    content_name = models.CharField("작품제목",max_length=50)
    content_period = models.CharField("기간",max_length=10)
    content_img = models.CharField("이미지", blank=True)

class Netflix_tvRank(models.Model):
    content_rank = models.CharField("순위",max_length=5)
    content_name = models.CharField("작품제목",max_length=50)
    content_period = models.CharField("기간",max_length=10)
    content_img = models.CharField("이미지", blank=True)

class Amazon_movieRank(models.Model):
    content_rank = models.CharField("순위",max_length=5)
    content_name = models.CharField("작품제목",max_length=50)
    content_period = models.CharField("기간",max_length=10, blank=True)
    content_img = models.CharField("이미지", blank=True)

class Amazon_tvRank(models.Model):
    content_rank = models.CharField("순위",max_length=5)
    content_name = models.CharField("작품제목",max_length=50)
    content_period = models.CharField("기간",max_length=10, blank=True)
    content_img = models.CharField("이미지", blank=True)

class Disney_Rank(models.Model):
    content_rank = models.CharField("순위",max_length=5)
    content_name = models.CharField("작품제목",max_length=50)
    content_period = models.CharField("기간",max_length=10)
    content_img = models.CharField("이미지", blank=True)

class Wavve_movieRank(models.Model):
    content_rank = models.CharField("순위",max_length=5)
    content_name = models.CharField("작품제목",max_length=50)
    content_period = models.CharField("기간",max_length=10)
    content_img = models.CharField("이미지", blank=True)

class Wavve_tvRank(models.Model):
    content_rank = models.CharField("순위",max_length=5)
    content_name = models.CharField("작품제목",max_length=50)
    content_period = models.CharField("기간",max_length=10)
    content_img = models.CharField("이미지", blank=True)