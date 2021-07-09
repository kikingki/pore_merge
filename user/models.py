from django.db import models
from django.contrib.auth.models import AbstractUser

# 분야
class Field(models.Model):
    def __str__(self):
        return self.field_name
    field_name = models.CharField(max_length=200)

# 경력
class Career(models.Model):
    def __str__(self):
        return self.user_ap
    user_ap = models.CharField(max_length=200)

# 커스텀 유저
class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

    name = models.CharField(max_length=200)     # username을 id로 사용해서 필요없는 이메일을 사용자 이름으로 변경
    nickname = models.CharField(max_length=200)
    account = models.CharField(max_length=200)
    cr_id = models.ForeignKey(Career, on_delete=models.CASCADE, related_name='users', null=True)
    field_id = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='users', null=True)