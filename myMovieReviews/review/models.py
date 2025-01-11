from django.db import models

# Create your models here.



class Review(models.Model):
    CATEGORY_CHOICES = [
        ('00', '코미디'),
        ('01', 'SF'),
        ('02', '액션'),
        ('03', '공포'),
        ('04', '다큐멘터리'),
        ('05', '로맨스'),
    ]
    
    
    title = models.TextField()      # 제목
    year = models.IntegerField()    # 개봉년도
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default='00'
        )   # 장르
    rating = models.DecimalField(max_digits=2, decimal_places=1)    # 별점
    runningTime = models.IntegerField()    # 러닝타임
    review = models.TextField()         # 리뷰
    director = models.TextField()       # 감독
    actor = models.TextField()          # 배우
    
