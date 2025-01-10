from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.TextField()      # 제목
    year = models.IntegerField()    # 개봉년도
    category = models.TextField()   # 장르
    rating = models.DecimalField(max_digits=2, decimal_places=1)    # 별점
    runningTime = models.TextField()    # 러닝타임
    review = models.TextField()         # 리뷰
    director = models.TextField()       # 감독
    actor = models.TextField()          # 배우
    
