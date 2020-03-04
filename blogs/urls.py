from django.urls improt path

from . import views

urlpatterns = [
    path = ('post/', views.posts_list, name='posts_list'),
    path = ('post/<int:post_id>', views.post_detail, name='post_detail'),
    path = ('comment/write', views.comment_write, name='comment_write'),
]