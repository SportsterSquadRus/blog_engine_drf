from django.db import models
from django.contrib import auth


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок поста')
    body = models.TextField(verbose_name='Текст поста')
    published = models.DateTimeField(null=True, blank=True)
    truncate = models.IntegerField(default=0)
    author = models.ForeignKey('auth.User', blank=True, null=True, on_delete=models.CASCADE)
    draft = models.BooleanField(verbose_name='Черновик', default=False)

