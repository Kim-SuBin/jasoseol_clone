from django.db import models

# 변경사항이 생겼을 때 makemigrations 사용
# 번역 파일은 migrations 폴더 안에 차곡차곡 쌓이고 이 파일을 migrate를 통해 db에 반영

# Create your models here.

class Jasoseol(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # auto_now=True 를 사용하면 업데이트 될 때마다 자동으로 현재 날짜와 시간 저장
    updated_at = models.DateTimeField(auto_now=True)