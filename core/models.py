from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)  # 电话号码
    avatar = models.ImageField(upload_to='media/accounts/', blank=True, null=True)  # 头像
    location = models.CharField(max_length=40, blank=True, null=True)  # 电话号码
    verified = models.BooleanField(default=False)   # 是否已验证
    
    def __str__(self):
        return self.username