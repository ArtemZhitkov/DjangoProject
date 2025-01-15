from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок статьи')
    content = models.TextField(verbose_name='Содержание статьи')
    preview = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    published = models.BooleanField()
    views_count = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']
