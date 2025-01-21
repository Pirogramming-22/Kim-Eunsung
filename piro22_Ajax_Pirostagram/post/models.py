from django.db import models
from user.models import User

# Create your models here.
class Post(models.Model):
    # 사진
    image = models.ImageField("사진", upload_to="img/%Y/%m/%d")
    # 작성자
    writer = models.ForeignKey(User, models.CASCADE, verbose_name="작성자", related_name="write_posts")
    # 본문
    content = models.TextField("본문")
    # 작성일시
    created_at = models.DateTimeField("작성일시", auto_now_add=True)
    
    # 좋아요 누른 사람들
    liker = models.ManyToManyField(User, through='Like', verbose_name="좋아요", related_name="like_posts")


class Comment(models.Model):
    # 대상 게시물
    post = models.ForeignKey(Post, models.CASCADE, verbose_name="대상 게시물")
    # 작성자
    writer = models.ForeignKey(User, models.CASCADE, verbose_name="작성자")
    # 본문
    content = models.TextField("본문")
    # 작성일시
    created_at = models.DateTimeField("작성일시", auto_now_add=True)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ensure a user can like a post only once
        unique_together = ('post', 'user')

    def __str__(self):
        return f"{self.user} liked {self.post}"