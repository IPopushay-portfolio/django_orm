from django.db import models

class Blog(models.Model):
    blog_name = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True)
    publication = models.BooleanField(default=True, verbose_name='Публикация')
    views_counter = models.PositiveIntegerField(verbose_name='Счетчик просмотров', default=0,
                                                help_text='Укажите количество просмотров')

    def __str__(self):
        return f'{self.blog_name}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['blog_name']
