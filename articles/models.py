from django.db import models
from accounts.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # user = models.ForeignKey()

# 유저 모델을 참조하는 경우
    # 1. (권장X) 유지보수 불편
# user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 2. settings.py
# user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 3.
user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
