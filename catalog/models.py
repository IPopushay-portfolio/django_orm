from django.db import models


class Category(models.Model):
    cat_name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', null=True)

    def __str__(self):
        return f'{self.cat_name} {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['cat_name']


class Product(models.Model):
    prod_name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', null=True)
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    category = models.CharField(verbose_name='Категория')
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    group = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.prod_name} {self.description}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['prod_name']

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='draft')
