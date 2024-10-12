
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # 추가 필드
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)  # 프로필 이미지 추가

    class Meta:
        db_table = 'user'  # 테이블 이름을 'user'로 설정

    def __str__(self):
        return self.username
