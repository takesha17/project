from distutils.command.upload import upload
from email import contentmanager
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=255,verbose_name="Название")
    content = models.TextField(verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to="post_images/", null=True)


class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE,verbose_name="Пост")
    content = models.TextField(verbose_name="Комментарий")
    user = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    