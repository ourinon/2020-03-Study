from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_fields):
        # Create and save a user with the given username, email, and password.
        # 함수 이름앞에 _는 클래스 안에서 사용하겠다는 명시적 표현이다.

        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(email=email, username=username **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_suer(self, email, username='', password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, username, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(max_length=255, verbose_name='email', unique=True)

    username = models.CharField(max_length=30)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = [] # 필수로 받고 싶은 필드를 넣기 원래 소스 코드엔 email필드가 들어가지만 우리는 로그인을 이메일로한다.

    def __str__(self):
        return "<%d %s>" %(self.pk, self.email)


# Model 작성
""" class Comment(models.Model):
    email = models.CharField(max_length=50, null=False)
    user = models.CharField(max_length=30, null=False)
    content = models.TextField(max_length=200, null=False)
    content_time = models.DateTimeField(auto_now_add=True) """

# Modle Relationship
# Mant-to-Many
# Many-to-One 직접 comment 모델은 해당 알고리즘
# One-to-One
