from django.db import models
from devtool.models import Devtool

# Create your models here.
class Idea(models.Model):
    title = models.CharField("아이디어명", max_length=20)
    image = models.ImageField("Image", upload_to="ideaImg/%Y/%m/%d")
    content = models.TextField("아이디어 설명")
    interest = models.IntegerField("아이디어 관심도", default=0)
    devtool = models.ForeignKey(Devtool, on_delete=models.CASCADE, verbose_name="예상 개발툴")
    zzim = models.BooleanField("찜", default=False)
