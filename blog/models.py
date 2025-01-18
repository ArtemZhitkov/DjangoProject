from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок статьи')
    content = models.TextField(verbose_name='Содержание статьи')
    preview = models.ImageField(upload_to='images/', verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    published = models.BooleanField(null=True)
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']
