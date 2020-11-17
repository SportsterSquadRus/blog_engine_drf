from django.db import models
from django.contrib import auth
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


    
class Like(models.Model):
    user = models.ForeignKey(
        auth.models.User, related_name='likes', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


    def __str__(self):
        return str(self.user)


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок поста')
    body = models.TextField(verbose_name='Текст поста')
    published = models.DateTimeField(
        null=True, blank=True, verbose_name='Дата публикации')
    truncate = models.IntegerField(default=0)
    author = models.ForeignKey(auth.models.User, blank=True,
                               null=True, on_delete=models.CASCADE, verbose_name='Автор')
    draft = models.BooleanField(verbose_name='Черновик', default=False)
    likes = GenericRelation(Like)

    @property
    def total_likes(self):
        return self.likes.count()

    def likeOrNot(self, user):
        return True if len(self.likes.filter(user=user)) == 0 else False

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    author = models.ForeignKey(
        auth.models.User, related_name='comment', on_delete=models.CASCADE, null=True)
    body = models.TextField(verbose_name='Текст комментярия')
    date_pub = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, verbose_name="Пост",
                             on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey('self', verbose_name="Родитель",
                               on_delete=models.CASCADE, blank=True, null=True, related_name="children")
    likes = GenericRelation(Like)

    @property
    def total_likes(self):
        return self.likes.count()


# {"title": "post2", "body": "lala<<hr />lolo", "author":1}
