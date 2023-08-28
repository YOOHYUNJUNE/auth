from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass # AbstractUser의 기능을 그대로 사용   
