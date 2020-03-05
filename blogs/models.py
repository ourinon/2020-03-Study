from django.db import models

from helpers.models import BaseModel
from users.models import User

from taggit.managers import TaggableManager

class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    tags = TaggableManager()
    
    def __str__(self):
        return '%s - %s' % (self.id, self.title)
    # 위 함수의 역할은 admin 사이트에 들어갔을경우 표현되는 objects들의 이름을
    # 내가 원하는 이름으로 설정하는 작업이다. 하위버전에는 유니코드를 작성함.

class Comment(BaseModle):
    post = models.ForignKey(Post, on_delete=CASCADE)
    user = models.ForignKey(User, on_delete=CASCADE)
    content = models.TextField()
    image = models.ImageField(balnk=True, null=True)
    likes = models.ManyToManyField(User, related_name='likes' blank=True)

    def __str__(self):
        return '%s - %s' % (self.id, self.user)

    def total_likes(self):
        return self.likes.count()


#Null 은 데이터베이스와 밀접한 연관. 데이베이스의 컬럼이 널가져올지 유무를 정함
#Blank 유효성과 관련이 있음. ex) is_vaild (에플리케이션)


